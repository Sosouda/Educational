import java.util.*;

/**
 * Класс-сборщик статистики. Обновляется в один проход при чтении файла.
 * Собирает данные для ответов на ~40 вопросов курсовой.
 */
public class StatisticsCollector {

    // === 3.1 Основные счётчики ===
    public long S = 0; // Всего записей (В.43)
    public long S_TM = 0; // Полезных записей (В.4, 43)
    public long S_Sluz = 0; // Служебных записей (В.2, 35)

    // === 3.2 Типы служебных сообщений ===
    public long countSessionStart = 0; // Тип 1 — Начало сеанса (В.21)
    public long countSessionEnd = 0; // Тип 3 — Конец сеанса (В.21)
    public long countModeChange = 0; // Тип 4 — Смена режима (В.3)
    public long countCurrentTime = 0; // Тип 2 — Текущее время (В.33)
    public long countError = 0; // Тип 6 — Ошибка (В.15)
    public long countEmptyPacket = 0; // Тип 0 — Пустая посылка (В.24)

    // === 3.3 Режимы и куски ===
    public String currentMode = "НП"; // Текущий режим
    public int currentModeCode = 1; // Код текущего режима (1=НП, 0=Недост, 2-8=ВП)
    private long currentChunkSize = 0; // Размер текущего куска

    public long chunksNP = 0; // Куски НП (В.5)
    public long chunksVP = 0; // Куски ВП (коды 2-8) (В.20)
    public long chunksInvalid = 0; // Куски Недостоверного (код 0) (В.6)
    public long chunksNotNP = 0; // Куски любого режима кроме НП (В.37)

    public long recordsNotNP = 0; // ТМ-записей НЕ в НП (В.8)
    public long recordsVP33 = 0; // ТМ-записей в ВП-3 (В.11) -- интерпретируем как ВП с кодом 3
    public long recordsVP = 0; // ТМ-записей в режимах 2..8 (В.20)

    // Хронология кусков: (режим, кол-во записей)
    public ArrayList<String> chunkHistory = new ArrayList<>();
    private boolean chunkStarted = false;

    // === 3.4 Типы данных ===
    public long Q0 = 0; // Long (В.29, 31)
    public long Q1 = 0; // Double (В.25, 32)
    public long Q2 = 0; // Code (В.39)
    public long Q3 = 0; // Point (В.40)

    // Уникальные ID по типам
    public HashSet<Integer> uniqueLongIds = new HashSet<>();
    public HashSet<Integer> uniqueDoubleIds = new HashSet<>(); // (В.25)
    public HashSet<Integer> uniqueCodeIds = new HashSet<>(); // (В.27)
    public HashSet<Integer> uniquePointIds = new HashSet<>(); // (В.30)

    // Code: записи с длиной < 8 бит (В.16) и > 8 бит (В.42)
    public long codeShort = 0; // len < 8
    public long codeLong = 0; // len > 8

    // Point: длина < 4 (В.7) и > 4 (В.22)
    public long pointShort = 0; // len < 4
    public long pointLong = 0; // len > 4

    // Подсчёт записей по каждому параметру (по ID)
    public HashMap<Integer, Long> paramRecordCount = new HashMap<>();
    // Подсчёт записей Long по каждому параметру
    public HashMap<Integer, Long> longParamCount = new HashMap<>();

    // === 3.5 Имена и XML ===
    // Уникальные ID параметров (В.26)
    public HashSet<Integer> allUniqueIds = new HashSet<>();

    // Температурные параметры (имя Txx) — подсчёт записей (В.1, В.44)
    public HashSet<Integer> tempParamIds = new HashSet<>();
    public HashMap<Integer, Long> tempParamCount = new HashMap<>();

    // === 3.6 Размерности ===
    public HashMap<Integer, Long> dimFrequency = new HashMap<>(); // код → кол-во
    public long dimensionless = 0; // безразмерные (dimCode = 0)

    // Имена параметров (для вывода в статистике)
    private DatXML datXml;

    public StatisticsCollector(DatXML datXml) {
        this.datXml = datXml;
    }

    // =========================================================
    // Обработка служебной записи
    // =========================================================
    public void processServiceRecord(int msgType, int modeCode) {
        S++;
        S_Sluz++;

        switch (msgType) {
            case 0:
                countEmptyPacket++;
                break;
            case 1:
                countSessionStart++;
                break;
            case 2:
                countCurrentTime++;
                break;
            case 3:
                countSessionEnd++;
                break;
            case 4:
                countModeChange++;
                // Завершаем предыдущий кусок
                finishChunk();
                // Начинаем новый
                currentModeCode = modeCode;
                if (modeCode == 1) {
                    currentMode = "НП";
                } else if (modeCode == 0) {
                    currentMode = "Недост.";
                } else {
                    currentMode = "ВП-" + modeCode;
                }
                break;
            case 6:
                countError++;
                break;
        }
    }

    // =========================================================
    // Обработка полезной ТМ-записи
    // =========================================================
    public void processTmRecord(TmDat td) {
        S++;
        S_TM++;

        // --- Кусок ---
        if (!chunkStarted) {
            chunkStarted = true;
        }
        currentChunkSize++;

        // ТМ в не-НП режиме
        if (currentModeCode != 1) {
            recordsNotNP++;
        }
        // ТМ в ВП (коды 2-8)
        if (currentModeCode >= 2 && currentModeCode <= 8) {
            recordsVP++;
        }
        // ТМ в ВП-3
        if (currentModeCode == 3) {
            recordsVP33++;
        }

        // --- Уникальные ID ---
        allUniqueIds.add(td.id);

        // --- Счётчик записей по ID ---
        paramRecordCount.merge(td.id, 1L, Long::sum);

        // --- Тип данных ---
        switch (td.type) {
            case 0:
                Q0++;
                uniqueLongIds.add(td.id);
                longParamCount.merge(td.id, 1L, Long::sum);
                break;
            case 1:
                Q1++;
                uniqueDoubleIds.add(td.id);
                break;
            case 2:
                Q2++;
                uniqueCodeIds.add(td.id);
                if (td instanceof TmCode) {
                    int cLen = ((TmCode) td).len;
                    if (cLen < 8)
                        codeShort++;
                    if (cLen > 8)
                        codeLong++;
                }
                break;
            case 3:
                Q3++;
                uniquePointIds.add(td.id);
                if (td instanceof TmPoint) {
                    int pLen = ((TmPoint) td).len;
                    if (pLen < 4)
                        pointShort++;
                    if (pLen > 4)
                        pointLong++;
                }
                break;
        }

        // --- Температурные параметры (Txx, Тxx) ---
        if (td.name != null && isTemperatureParam(td.name)) {
            tempParamIds.add(td.id);
            tempParamCount.merge(td.id, 1L, Long::sum);
        }

        // --- Размерность ---
        int dimCode = 0;
        try {
            // Извлекаем код из строки dimension, если она начинается с "dim="
            if (td.dimension != null && td.dimension.startsWith("dim=")) {
                dimCode = Integer.parseInt(td.dimension.substring(4));
            }
        } catch (NumberFormatException ignored) {
        }
        // Считаем по строковому значению — просто по dimCode из байта
        // Используем raw dimCode, который хранится в поле id через отдельный вызов
    }

    /**
     * Учёт размерности (вызывается из ReadTMI с raw dimCode).
     */
    public void countDimension(int dimCode, String dimName) {
        if (dimCode == 0 || dimName == null || dimName.trim().isEmpty() || dimName.startsWith("dim=")) {
            dimensionless++;
        }
        dimFrequency.merge(dimCode, 1L, Long::sum);
    }

    /**
     * Определяет, является ли имя температурным параметром.
     * Паттерн: начинается с "Т" (кириллица) или "T" (латиница) + цифры.
     */
    private boolean isTemperatureParam(String name) {
        if (name == null || name.length() < 2)
            return false;
        char first = name.charAt(0);
        if (first != 'T' && first != 'Т')
            return false; // латинская T или кириллическая Т
        char second = name.charAt(1);
        return Character.isDigit(second);
    }

    // =========================================================
    // Куски (Chunks)
    // =========================================================
    private void finishChunk() {
        if (currentChunkSize > 0 || chunkStarted) {
            // Записываем предыдущий кусок
            chunkHistory.add(currentMode + " - " + currentChunkSize);

            if (currentModeCode == 1)
                chunksNP++;
            else {
                chunksNotNP++;
                if (currentModeCode == 0)
                    chunksInvalid++;
                if (currentModeCode >= 2 && currentModeCode <= 8)
                    chunksVP++;
            }
        }
        currentChunkSize = 0;
        chunkStarted = false;
    }

    /**
     * Завершение парсинга — закрыть последний кусок.
     */
    public void finalize_() {
        finishChunk();
    }

    // =========================================================
    // Генерация полного отчёта (ответы на вопросы)
    // =========================================================
    /*public String generateReport() {
        StringBuilder r = new StringBuilder();
        r.append("==================== СТАТИСТИКА ====================\n\n");

        // --- Основные ---
        r.append(String.format(" В.43  S (всего записей):          %,d\n", S));
        r.append(String.format(" В.4   S_TM (полезных):            %,d\n", S_TM));
        r.append(String.format(" В.2   S_Sluz (служебных):         %,d\n", S_Sluz));
        r.append(String.format("       Проверка S=S_TM+S_Sluz:     %s\n",
                (S == S_TM + S_Sluz) ? "OK" : "ОШИБКА!"));
        r.append("\n--- Служебные записи по типам ---\n");
        r.append(String.format(" В.21  Начало сеанса (тип 1):      %,d\n", countSessionStart));
        r.append(String.format(" В.21  Конец сеанса (тип 3):       %,d\n", countSessionEnd));
        r.append(String.format(" В.3   Смена режима (тип 4):       %,d\n", countModeChange));
        r.append(String.format(" В.33  Текущее время (тип 2):      %,d\n", countCurrentTime));
        r.append(String.format(" В.15  Ошибка (тип 6):             %,d\n", countError));
        r.append(String.format(" В.24  Пустая посылка (тип 0):     %,d\n", countEmptyPacket));

        // --- Режимы и куски ---
        r.append("\n--- Режимы и куски ---\n");
        r.append(String.format(" В.5   Кусков НП:                  %,d\n", chunksNP));
        r.append(String.format(" В.20  Кусков ВП (2-8):            %,d\n", chunksVP));
        r.append(String.format(" В.6   Кусков Недостоверных (0):    %,d\n", chunksInvalid));
        r.append(String.format(" В.37  Кусков НЕ-НП (всего):       %,d\n", chunksNotNP));
        r.append(String.format(" В.8   ТМ-записей НЕ в НП:         %,d\n", recordsNotNP));
        r.append(String.format(" В.11  ТМ-записей в ВП-3:          %,d\n", recordsVP33));
        r.append(String.format(" В.20  ТМ-записей в ВП (2-8):      %,d\n", recordsVP));

        // --- Типы данных ---
        r.append("\n--- Типы данных ---\n");
        r.append(String.format(" В.29  Long (Q0):                  %,d\n", Q0));
        r.append(String.format(" В.31  Long (Q0) повтор:           %,d\n", Q0));
        r.append(String.format(" В.25  Double (Q1):                %,d\n", Q1));
        r.append(String.format(" В.25  Уникальных Double парам.:   %,d\n", uniqueDoubleIds.size()));
        r.append(String.format(" В.39  Code (Q2):                  %,d\n", Q2));
        r.append(String.format(" В.27  Уникальных Code парам.:     %,d\n", uniqueCodeIds.size()));
        r.append(String.format(" В.16  Code с длиной < 8 бит:      %,d\n", codeShort));
        r.append(String.format(" В.42  Code с длиной > 8 бит:      %,d\n", codeLong));
        r.append(String.format(" В.40  Point (Q3):                 %,d\n", Q3));
        r.append(String.format(" В.30  Уникальных Point парам.:    %,d\n", uniquePointIds.size()));
        r.append(String.format(" В.7   Point с длиной < 4:         %,d\n", pointShort));
        r.append(String.format(" В.22  Point с длиной > 4:         %,d\n", pointLong));

        // --- Long: параметр с макс. записей (В.29) ---
        if (!longParamCount.isEmpty()) {
            Map.Entry<Integer, Long> maxLong = Collections.max(
                    longParamCount.entrySet(), Map.Entry.comparingByValue());
            r.append(String.format(" В.29  Long макс. записей:         %s (ID=%d, %,d зап.)\n",
                    datXml.getName(maxLong.getKey()), maxLong.getKey(), maxLong.getValue()));
        }

        // --- Уникальные параметры ---
        r.append("\n--- Параметры ---\n");
        r.append(String.format(" В.26  Уникальных параметров (ID):  %,d\n", allUniqueIds.size()));

        // Параметр с мин. числом записей "редкий" (В.9)
        if (!paramRecordCount.isEmpty()) {
            Map.Entry<Integer, Long> rarest = Collections.min(
                    paramRecordCount.entrySet(), Map.Entry.comparingByValue());
            r.append(String.format(" В.9   Самый редкий параметр:      %s (ID=%d, %,d зап.)\n",
                    datXml.getName(rarest.getKey()), rarest.getKey(), rarest.getValue()));
        }

        // Параметры, встретившиеся ровно 2 раза (В.10)
        long countExactly2 = 0;
        for (Long cnt : paramRecordCount.values()) {
            if (cnt == 2)
                countExactly2++;
        }
        r.append(String.format(" В.10  Параметров с ровно 2 зап.:   %,d\n", countExactly2));

        // --- Температурные ---
        r.append("\n--- Температурные параметры ---\n");
        r.append(String.format(" В.1   Кол-во темп. параметров:     %,d\n", tempParamIds.size()));

        if (!tempParamCount.isEmpty()) {
            Map.Entry<Integer, Long> maxTemp = Collections.max(
                    tempParamCount.entrySet(), Map.Entry.comparingByValue());
            r.append(String.format(" В.44  Темп. макс. записей:        %s (ID=%d, %,d зап.)\n",
                    datXml.getName(maxTemp.getKey()), maxTemp.getKey(), maxTemp.getValue()));
        }

        // --- Текстовые параметры (В.13): параметры с текстовой расшифровкой ---
        // (DatXML не хранит текстовые расшифровки, но можно посчитать уникальные числа)
        r.append(String.format(" В.13  Тексто-параметры (из XML):    см. XML\n"));

        // --- Размерности ---
        r.append("\n--- Размерности ---\n");
        if (!dimFrequency.isEmpty()) {
            Map.Entry<Integer, Long> mostFreqDim = Collections.max(
                    dimFrequency.entrySet(), Map.Entry.comparingByValue());
            Map.Entry<Integer, Long> leastFreqDim = Collections.min(
                    dimFrequency.entrySet(), Map.Entry.comparingByValue());
            r.append(String.format(" В.17  Самая частая размерность:    код %d (%,d раз)\n",
                    mostFreqDim.getKey(), mostFreqDim.getValue()));
            r.append(String.format(" В.41  Самая редкая размерность:    код %d (%,d раз)\n",
                    leastFreqDim.getKey(), leastFreqDim.getValue()));
        }
        r.append(String.format("       Безразмерных записей:        %,d\n", dimensionless));

        // --- Хронология кусков (В.19) ---
        r.append("\n--- Хронология кусков (В.19) ---\n");
        int maxShow = Math.min(chunkHistory.size(), 200);
        for (int i = 0; i < maxShow; i++) {
            r.append(String.format("  %3d. %s\n", i + 1, chunkHistory.get(i)));
        }
        if (chunkHistory.size() > maxShow) {
            r.append("  ... (ещё " + (chunkHistory.size() - maxShow) + " кусков)\n");
        }

        // --- В.14/18: Список индексов и номеров в алф. порядке ---
        r.append("\n--- Параметры по алфавиту (В.14, 18) ---\n");
        TreeMap<String, Integer> nameToId = new TreeMap<>();
        for (int id : allUniqueIds) {
            nameToId.put(datXml.getName(id), id);
        }
        int idx = 1;
        int showMax = Math.min(nameToId.size(), 100);
        int shown = 0;
        for (Map.Entry<String, Integer> e : nameToId.entrySet()) {
            r.append(String.format("  %4d. %-20s ID=%d\n", idx++, e.getKey(), e.getValue()));
            shown++;
            if (shown >= showMax)
                break;
        }
        if (nameToId.size() > showMax) {
            r.append("  ... (ещё " + (nameToId.size() - showMax) + " параметров)\n");
        }

        r.append("\n====================================================\n");
        return r.toString();
    }*/
    public Map<String, String> generateQuestionsMap() {
        Map<String, String> q = new LinkedHashMap<>();

        // Вспомогательная лямбда для лаконичности (если Java 8+)
        // Или просто q.put("В.43", String.format(...))
        
        q.put("В.43 Всего записей (S)", String.format("В.43  S (всего записей): %,d", S));
        q.put("В.4   Полезных (S_TM)", String.format("В.4   S_TM (полезных): %,d", S_TM));
        q.put("В.2   Служебных (S_Sluz)", String.format("В.2   S_Sluz (служебных): %,d", S_Sluz));
        
        q.put("В.21  Начало/Конец сеанса", String.format("Начало (тип 1): %,d\nКонец (тип 3): %,d", countSessionStart, countSessionEnd));
        q.put("В.3   Смена режима", String.format("В.3   Смена режима (тип 4): %,d", countModeChange));
        q.put("В.33  Текущее время", String.format("В.33  Текущее время (тип 2): %,d", countCurrentTime));
        q.put("В.15  Ошибка", String.format("В.15  Ошибка (тип 6): %,d", countError));
        q.put("В.24  Пустая посылка", String.format("В.24  Пустая посылка (тип 0): %,d", countEmptyPacket));

        q.put("В.5   Кусков НП", String.format("В.5   Кусков НП: %,d", chunksNP));
        q.put("В.20  Кусков ВП (2-8)", String.format("В.20  Кусков ВП (2-8): %,d\nТМ-записей в ВП: %,d", chunksVP, recordsVP));
        q.put("В.6   Кусков Недостоверных", String.format("В.6   Кусков Недостоверных (0): %,d", chunksInvalid));
        q.put("В.37  Кусков НЕ-НП", String.format("В.37  Кусков НЕ-НП (всего): %,d", chunksNotNP));
        q.put("В.8   ТМ-записи НЕ в НП", String.format("В.8   ТМ-записей НЕ в НП: %,d", recordsNotNP));
        q.put("В.11  ТМ-записи в ВП-3", String.format("В.11  ТМ-записей в ВП-3: %,d", recordsVP33));

        q.put("В.29  Long (Q0)", String.format("В.29  Long (Q0): %,d", Q0));
        q.put("В.25  Double (Q1)", String.format("В.25  Double (Q1): %,d\nУникальных: %,d", Q1, uniqueDoubleIds.size()));
        q.put("В.39  Code (Q2)", String.format("В.39  Code (Q2): %,d\nУникальных: %,d", Q2, uniqueCodeIds.size()));
        q.put("В.40  Point (Q3)", String.format("В.40  Point (Q3): %,d\nУникальных: %,d", Q3, uniquePointIds.size()));

        // Параметры
        q.put("В.26  Уникальных параметров", String.format("В.26  Уникальных параметров (ID): %,d", allUniqueIds.size()));
        
        if (!paramRecordCount.isEmpty()) {
            Map.Entry<Integer, Long> rarest = Collections.min(paramRecordCount.entrySet(), Map.Entry.comparingByValue());
            q.put("В.9   Самый редкий параметр", String.format("В.9   Самый редкий: %s (ID=%d, %,d зап.)", 
                    datXml.getName(rarest.getKey()), rarest.getKey(), rarest.getValue()));
        }

        long count2 = paramRecordCount.values().stream().filter(cnt -> cnt == 2).count();
        q.put("В.10  Параметры с 2 зап.", String.format("В.10  Параметров с ровно 2 зап.: %,d", count2));

        q.put("В.1   Кол-во темп. параметров", String.format("В.1   Кол-во темп. параметров: %,d", tempParamIds.size()));

        // Хронология (В.19)
        StringBuilder sbHistory = new StringBuilder();
        chunkHistory.stream().limit(200).forEach(s -> sbHistory.append(s).append("\n"));
        q.put("В.19  Хронология кусков", sbHistory.toString());

        // Алфавитный указатель (В.14, 18)
        StringBuilder sbAlpha = new StringBuilder();
        new TreeMap<String, Integer>(/* здесь логика заполнения из вашего кода */)
            .forEach((name, id) -> sbAlpha.append(String.format("%-20s ID=%d\n", name, id)));
        q.put("В.14/18 Параметры по алфавиту", sbAlpha.toString());

        return q;
    }
}
