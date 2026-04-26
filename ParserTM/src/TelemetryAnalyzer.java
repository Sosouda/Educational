import java.io.*;
import java.util.*;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

public class TelemetryAnalyzer {

    private final String XML_FILE = "KNP-173.14.33.58.dat.xml";
    private final String KNP_FILE = "190829_v29854.KNP";

    private final int TYPE_LONG = 0;
    private final int TYPE_DOUBLE = 1;
    private final int TYPE_CODE = 2;
    private final int TYPE_POINT = 3;
    private final int ID_SERVICE = 0xFFFF;

    // Режимы из служебных записей
    private final int MODE_NP = 1;      // Режим НП (научная программа)
    private final int MODE_VPZZ = 2;    // Режим ВПЗЗ (выдача программы целевого задания)
    private final int MODE_INVALID = 3; // Недостоверный режим

    private boolean isAnalyzed = false;
    
    // Задача 1: температурные параметры из XML
    private int countTempParamsXML = 0;

    // Задача 2: служебные записи (ID=0xFFFF)
    private int countServiceRecords = 0;
    
    // Задача 3: служебные записи типа "смена режима" (dimOrMsgType == 1)
    private int countModeChangeRecords = 0;
    
    // Задача 4: полезные записи (не служебные)
    private int countUsefulRecords = 0;
    
    // Задача 5: смена режима со значением "режим НП"
    private int countModeNP = 0;
    
    // Задача 6: смена режима со значением "недостоверный режим"
    private int countModeInvalid = 0;
    
    // Задача 7: Point с длиной < 4 байт
    private int countPointLess4 = 0;
    
    // Задача 8: записи вне режима НП
    private int countNotNP = 0;
    
    // Задача 9: параметр с наименьшим кол-вом записей
    private String paramWithMinRecords = "Н/Д";
    
    // Задача 10: параметры с двумя записями
    private List<Integer> paramsWithTwoRecords = new ArrayList<>();
    
    // Задача 11: кол-во записей по режимам
    private int countRecordsInNP = 0;
    private int countRecordsInVPZZ = 0;
    private int countRecordsInOther = 0;
    
    // Задача 12: проверка совпадения
    private int totalParams = 0;
    private int sumByTypes = 0;
    private String typeCheckResult = "Н/Д";

    // Для подсчёта частоты параметров
    private Map<Integer, Integer> paramFrequency = new HashMap<>();
    
    // Текущий режим
    private int currentMode = MODE_INVALID;

    public String getAnswer(int questionNumber) {
        if (!isAnalyzed) {
            analyzeXML();
            analyzeKNP();
            isAnalyzed = true;
        }

        switch (questionNumber) {
            case 1: return String.valueOf(countTempParamsXML);
            case 2: return String.valueOf(countServiceRecords);
            case 3: return String.valueOf(countModeChangeRecords);
            case 4: return String.valueOf(countUsefulRecords);
            case 5: return String.valueOf(countModeNP);
            case 6: return String.valueOf(countModeInvalid);
            case 7: return String.valueOf(countPointLess4);
            case 8: return String.valueOf(countNotNP);
            case 9: return paramWithMinRecords;
            case 10: return paramsWithTwoRecords.isEmpty() ? "Нет" : paramsWithTwoRecords.toString();
            case 11: return "НП: " + countRecordsInNP + ", ВПЗЗ: " + countRecordsInVPZZ + ", Другие: " + countRecordsInOther;
            case 12: return typeCheckResult;
            default: return "Нет данных";
        }
    }

    private void analyzeXML() {
        try {
            File file = new File(XML_FILE);
            if (!file.exists()) return;

            DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
            DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
            Document doc = dBuilder.parse(file);
            doc.getDocumentElement().normalize();

            NodeList nList = doc.getElementsByTagName("Param");

            for (int i = 0; i < nList.getLength(); i++) {
                Node nNode = nList.item(i);
                if (nNode.getNodeType() == Node.ELEMENT_NODE) {
                    Element eElement = (Element) nNode;
                    String name = eElement.getAttribute("name");
                    if (name.startsWith("Т") || name.startsWith("T")) {
                        countTempParamsXML++;
                    }
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void analyzeKNP() {
        File file = new File(KNP_FILE);
        if (!file.exists()) return;

        try (DataInputStream dis = new DataInputStream(new BufferedInputStream(new FileInputStream(file)))) {
            while (dis.available() > 0) {
                int id = dis.readUnsignedShort();      // 0-1 байты: Номер параметра
                int time = dis.readInt();              // 2-5 байты: Время
                int dimOrMsgType = dis.readUnsignedByte(); // 6 байт: Размерность (или Тип сообщения)
                int attrAndType = dis.readUnsignedByte();  // 7 байт: Атрибут и Тип значения

                if (id == ID_SERVICE) {
                    countServiceRecords++;

                    // Обработка служебных записей
                    // Тип сообщения в байте 6:
                    // 1 - начало сеанса (длина 24 байта)
                    // 4 - смена режима (длина 8 байт)
                    // 6 - ошибка
                    
                    if (dimOrMsgType == 4) {
                        // Смена режима
                        countModeChangeRecords++;
                        
                        // Байты 8-11: не используются
                        dis.skipBytes(4);
                        
                        // Байты 12-15: номер режима (целое 32-bit)
                        int modeValue = dis.readInt();
                        
                        if (modeValue == MODE_NP) {
                            countModeNP++;
                            currentMode = MODE_NP;
                        } else if (modeValue == 0) {
                            countModeInvalid++;
                            currentMode = MODE_INVALID;
                        } else {
                            // Все остальные режимы - ВП (2-33 и другие)
                            currentMode = MODE_VPZZ;
                        }
                    } else if (dimOrMsgType == 1) {
                        // Начало сеанса - длина 24 байта
                        dis.skipBytes(24);
                    } else if (dimOrMsgType == 6) {
                        // Ошибка - длина 8 байт
                        dis.skipBytes(8);
                    } else {
                        // Другие служебные - длина 8 байт
                        dis.skipBytes(8);
                    }

                } else {
                    // Полезная запись
                    countUsefulRecords++;
                    paramFrequency.put(id, paramFrequency.getOrDefault(id, 0) + 1);
                    totalParams++;

                    // Подсчёт по режимам (задача 11)
                    if (currentMode == MODE_NP) {
                        countRecordsInNP++;
                    } else if (currentMode == MODE_VPZZ) {
                        countRecordsInVPZZ++;
                    } else {
                        countRecordsInOther++;
                        countNotNP++; // задача 8
                    }

                    int type = attrAndType & 0x0F;
                    sumByTypes++;

                    if (type == TYPE_LONG) {
                        dis.skipBytes(8);

                    } else if (type == TYPE_DOUBLE) {
                        dis.skipBytes(8);

                    } else if (type == TYPE_CODE) {
                        dis.skipBytes(8);

                    } else if (type == TYPE_POINT) {
                        int elemSize = dis.readUnsignedByte(); // 8-й байт
                        int seqLen = dis.readUnsignedByte();   // 9-й байт

                        if (seqLen < 4) countPointLess4++;

                        dis.skipBytes(seqLen);

                    } else {
                        dis.skipBytes(8);
                    }
                }
            }
            calculateMinFreqParam();
            calculateTypeCheck();

        } catch (EOFException e) {
            calculateMinFreqParam();
            calculateTypeCheck();
        } catch (Exception e) {
            e.printStackTrace();
            calculateMinFreqParam();
            calculateTypeCheck();
        }
    }

    private void calculateMinFreqParam() {
        if (paramFrequency.isEmpty()) return;

        int minCount = Integer.MAX_VALUE;
        int minId = -1;
        paramsWithTwoRecords.clear();

        for (Map.Entry<Integer, Integer> entry : paramFrequency.entrySet()) {
            int count = entry.getValue();
            int id = entry.getKey();
            
            if (count < minCount) {
                minCount = count;
                minId = id;
            }
            if (count == 2) {
                paramsWithTwoRecords.add(id);
            }
        }
        paramWithMinRecords = "ID: " + minId + " (" + minCount + " шт.)";
    }
    
    private void calculateTypeCheck() {
        // Задача 12: проверяем совпадение общего кол-ва параметров с суммой по типам
        if (totalParams == sumByTypes) {
            typeCheckResult = "Совпадает: " + totalParams + " == " + sumByTypes;
        } else {
            typeCheckResult = "НЕ совпадает: " + totalParams + " != " + sumByTypes;
        }
    }
}