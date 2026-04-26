/**
 * ТМ-запись типа Code (кодовое значение).
 * Тип значения = 2. Байт 11 = длина кода, байты 12-15 = значение.
 */
public class TmCode extends TmDat {
    public int len;
    public String value; // битовая строка

    public TmCode(String name, int id, long time, String dimension, int type) {
        super(name, id, time, dimension, type);
    }

    @Override
    public String getValueString() {
        return value + " (len=" + len + ")";
    }
}
