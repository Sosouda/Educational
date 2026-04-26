import java.io.*;
import java.nio.charset.Charset;
import java.util.ArrayList;

public class ReadTMI {
    private String inputFile;
    private DatXML datXml;
    private Dim dim;

    public ArrayList<TmDat> records = new ArrayList<>();
    public StatisticsCollector stats;
    public String sessionInfo = "";

    public ReadTMI(String inputFile, DatXML datXml, Dim dim) {
        this.inputFile = inputFile;
        this.datXml = datXml;
        this.dim = dim;
        this.stats = new StatisticsCollector(datXml);
    }

    public void load() {
        byte[] buff = new byte[90000];

        try (FileInputStream fis = new FileInputStream(inputFile)) {
            // First record - Session Start (32 bytes)
            int read = fis.read(buff, 0, 32);
            if (read < 32) {
                System.out.println("File too small.");
                return;
            }
            int firstMsgType = buff[6] & 0xFF;
            stats.processServiceRecord(firstMsgType, stats.currentModeCode);
            extractSessionInfo(buff);

            // Main loop: read 16 bytes
            while (fis.read(buff, 0, 16) == 16) {
                int id = ((buff[0] & 0xFF) << 8) | (buff[1] & 0xFF);

                if (id == 0xFFFF) {
                    // Service record
                    int msgType = buff[6] & 0xFF;
                    int modeCode = stats.currentModeCode;

                    if (msgType == 1) {
                        // Session Start - read 16 more bytes
                        fis.read(buff, 16, 16);
                        extractSessionInfo(buff);
                    } else if (msgType == 4) {
                        // Mode change
                        modeCode = ((buff[14] & 0xFF) << 8) | (buff[15] & 0xFF);
                    }

                    stats.processServiceRecord(msgType, modeCode);
                } else {
                    // TM record
                    TmDat td = createTmDat(buff, fis, id);
                    if (td != null) {
                        records.add(td);
                        int dimCode = buff[6] & 0xFF;
                        String dimension = dim.get(dimCode); 
                        stats.countDimension(dimCode, dimension);
                        stats.processTmRecord(td);
                    }
                }
            }
            stats.finalize_();

        } catch (FileNotFoundException e) {
            System.out.println("File not found: " + inputFile);
        } catch (IOException e) {
            System.out.println("Read error: " + e.getMessage());
        }
    }

    private void extractSessionInfo(byte[] buff) {
        // Decode bytes 8-31 using Windows-1251 to support Cyrillic headers
        String raw = new String(buff, 8, 24, Charset.forName("Cp1251")).trim();
        if (!raw.isEmpty()) {
            sessionInfo = "Session Start: " + raw;
        }
    }

    private TmDat createTmDat(byte[] buff, FileInputStream fis, int id) throws IOException {
        long time = ((long) (buff[2] & 0xFF) << 24) |
                ((long) (buff[3] & 0xFF) << 16) |
                ((long) (buff[4] & 0xFF) << 8) |
                ((long) (buff[5] & 0xFF));

        int dimCode = buff[6] & 0xFF;
        String dimension = dim.get(dimCode);
        int typeVal = buff[7] & 0x0F;
        String name = datXml.getName(id);

        TmDat td = null;

        switch (typeVal) {
            case 0: // Long
                td = new TmLong(name, id, time, dimension, typeVal);
                long lng = ((long) (buff[12] & 0xFF) << 24) |
                        ((long) (buff[13] & 0xFF) << 16) |
                        ((long) (buff[14] & 0xFF) << 8) |
                        ((long) (buff[15] & 0xFF));
                ((TmLong) td).value = lng;
                break;

            case 1: // Double
                td = new TmDouble(name, id, time, dimension, typeVal);
                double dbl = java.nio.ByteBuffer.wrap(new byte[] {
                        buff[8], buff[9], buff[10], buff[11],
                        buff[12], buff[13], buff[14], buff[15]
                }).getDouble();
                ((TmDouble) td).value = dbl;
                break;

            case 2: // Code
                td = new TmCode(name, id, time, dimension, typeVal);
                int codeLen = ((buff[10] & 0xFF) << 8) | (buff[11] & 0xFF);
                String s = "";
                int numByte = (codeLen - 1) / 8;
                int numBit = (codeLen - 1) % 8;
                while (true) {
                    s = s + ((buff[15 - numByte] >> numBit) & 0x1);
                    numBit--;
                    if (numBit < 0) {
                        numBit += 8;
                        numByte--;
                    }
                    if (numByte < 0)
                        break;
                }
                ((TmCode) td).len = codeLen;
                ((TmCode) td).value = s;
                break;

            case 3: // Point
                td = new TmPoint(name, id, time, dimension, typeVal);
                int elemSize = buff[8] & 0xFF;
                int dataLen = ((buff[10] & 0xFF) << 8) | (buff[11] & 0xFF);
                ((TmPoint) td).elemSize = elemSize;
                ((TmPoint) td).len = dataLen;

                if (dataLen > 4) {
                    byte[] extraData = new byte[dataLen - 4];
                    byte[] allData = new byte[dataLen];
                    allData[0] = buff[12];
                    allData[1] = buff[13];
                    allData[2] = buff[14];
                    allData[3] = buff[15];
                    fis.read(extraData, 0, dataLen - 4);
                    System.arraycopy(extraData, 0, allData, 4, dataLen - 4);
                    ((TmPoint) td).data = allData;
                } else {
                    byte[] pointData = new byte[dataLen];
                    for (int i = 0; i < dataLen && (12 + i) < 16; i++) {
                        pointData[i] = buff[12 + i];
                    }
                    ((TmPoint) td).data = pointData;
                }
                break;

            default:
                return null;
        }
        return td;
    }
}