/**
 * ТМ-запись типа Long (32-битное целое).
 * Тип значения = 0. Байты 12-15.
 */
public class TmLong extends TmDat {
    public long value;

    public TmLong(String name, int id, long time, String dimension, int type) {
        super(name, id, time, dimension, type);
    }

    @Override
    public String getValueString() {
        return String.valueOf(value);
    }
}
