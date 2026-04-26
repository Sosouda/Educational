/**
 * ТМ-запись типа Point (массив байт).
 * Тип значения = 3. Байт 8 = размер элемента, байты 10-11 = длина массива в
 * байтах.
 * Если длина > 4, запись продолжается за пределами стандартных 16 байт.
 */
public class TmPoint extends TmDat {
    public int len; // длина массива в байтах
    public int elemSize; // размер элемента
    public byte[] data; // данные массива

    public TmPoint(String name, int id, long time, String dimension, int type) {
        super(name, id, time, dimension, type);
    }

    @Override
    public String getValueString() {
        if (data == null || data.length == 0)
            return "[Point len=" + len + "]";
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        int limit = Math.min(data.length, 16); // показываем не более 16 байт
        for (int i = 0; i < limit; i++) {
            if (i > 0)
                sb.append(" ");
            sb.append(String.format("%02X", data[i] & 0xFF));
        }
        if (data.length > limit)
            sb.append("...");
        sb.append("] (len=").append(len).append(")");
        return sb.toString();
    }
}
