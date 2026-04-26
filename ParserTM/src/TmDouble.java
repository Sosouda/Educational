/**
 * ТМ-запись типа Double (64-битное вещественное).
 * Тип значения = 1. Байты 8-15.
 */
public class TmDouble extends TmDat {
    public double value;

    public TmDouble(String name, int id, long time, String dimension, int type) {
        super(name, id, time, dimension, type);
    }

    @Override
    public String getValueString() {
        return String.format("%.6f", value);
    }
}
