/**
 * Базовый абстрактный класс для телеметрической записи.
 */
public abstract class TmDat implements Comparable<TmDat> {
    public int id;
    public long time; // мс от начала суток
    public String name;
    public String dimension;
    public int type;

    public TmDat(String name, int id, long time, String dimension, int type) {
        this.name = (name != null) ? name : "Unknown";
        this.id = id;
        this.time = time;
        this.dimension = (dimension != null) ? dimension : "";
        this.type = type;
    }

    /**
     * Конвертирует время (мс от начала суток) в строку ЧЧ:ММ:СС.ммм
     */
    public String getTimeString() {
        long ms = time;
        long hours = ms / 3600000;
        ms %= 3600000;
        long minutes = ms / 60000;
        ms %= 60000;
        long seconds = ms / 1000;
        long millis = ms % 1000;
        return String.format("%02d:%02d:%02d.%03d", hours, minutes, seconds, millis);
    }

    /**
     * Возвращает строковое представление значения параметра.
     */
    public abstract String getValueString();

    @Override
    public int compareTo(TmDat other) {
        return this.name.compareTo(other.name);
    }

    @Override
    public String toString() {
        return String.format("%-20s %s  %-20s %s", name, getTimeString(), getValueString(), dimension);
    }
}
