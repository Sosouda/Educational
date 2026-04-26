/*
 * =============================================================================
 * Класс: Main
 *
 * Назначение:
 * Главный класс приложения. Реализует графический интерфейс 
 * и управляет работой программы: запуск парсинга, отображение данных,
 * вывод статистики и обработка ошибок.
 *
 * ---------------------------------------------------------------------------
 * 1. Константы
 *
 * APP_TITLE    – заголовок главного окна.
 * FILE_KNP     – путь к входному файлу формата KNP.
 * FILE_XML     – путь к входному XML-файлу.
 * FILE_DIM     – путь к дополнительному файлу DIM.
 *
 * WIN_WIDTH    – ширина окна.
 * WIN_HEIGHT   – высота окна.
 * DIVIDER_LOC  – положение разделителя (если используется JSplitPane).
 *
 * ---------------------------------------------------------------------------
 * 2. Поля класса
 *
 * mainFrame    (JFrame)           – главное окно приложения.
 * listModel    (DefaultListModel) – модель данных для списка параметров.
 * paramList    (JList)            – список уникальных параметров.
 * dataArea     (JTextArea)        – область для вывода данных и истории.
 * statusLabel  (JLabel)           – строка состояния.
 *
 * telemetryReader (ReadTMI)       – объект парсера, который читает файл
 *                                    и хранит полученные данные.
 *
 * ---------------------------------------------------------------------------
 * 3. Методы класса
 *
 * main(String[] args)
 *   Точка входа в программу. Создаёт объект Main и запускает GUI.
 *
 * Main()
 *   Конструктор. Создаёт и настраивает все элементы интерфейса,
 *   размещает их в окне и регистрирует обработчики событий.
 *
 * show()
 *   Делает главное окно видимым.
 *
 * startParsing()
 *   Запускает процесс чтения и разбора файла в отдельном потоке,
 *   чтобы интерфейс не "зависал".
 *
 * updateUIOnSuccess(long time)
 *   Вызывается после успешного завершения парсинга.
 *   Обновляет список параметров и статус.
 *
 * updateUIOnError(Exception e)
 *   Вызывается при ошибке во время парсинга.
 *   Показывает сообщение об ошибке пользователю.
 *
 * displayParameterHistory(String paramName)
 *   Отображает историю значений выбранного параметра
 *   в виде отформатированной таблицы в dataArea.
 *
 * showStatisticsDialog()
 *   Открывает отдельное окно со сводной статистикой.
 *
 * ---------------------------------------------------------------------------
 * 4. Методы создания компонентов (вспомогательные)
 *
 * createParameterList() – создаёт и настраивает список параметров.
 * createDataArea()      – создаёт текстовую область для вывода данных.
 * createControlPanel()  – создаёт панель с кнопками управления.
 *
 */


import java.awt.*;
import java.util.*;
import java.util.List;
import javax.swing.*;

public class Main {

    private static final String APP_TITLE = "Телеметрия";
    private static final String FILE_KNP = "190829_v29854.KNP";
    private static final String FILE_XML = "KNP-173.14.33.58.dat.xml";
    private static final String FILE_DIM = "dimens.ion";
    
    private static final int WIN_WIDTH = 1600;
    private static final int WIN_HEIGHT = 1000;
    private static final int DIVIDER_LOC = 500;

    private final JFrame mainFrame;
    private final JList<String> paramList;
    private final JTextArea dataArea;
    private final JLabel statusLabel;
    private final DefaultListModel<String> listModel;
    private final JComboBox<String> dimensionFilter;

    private ReadTMI telemetryReader;
    private java.util.List<String> allParameters;

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            Main app = new Main();
            app.show();
            app.startParsing();
        });
    }

    public Main() {
        listModel = new DefaultListModel<>();
        allParameters = new ArrayList<>();

        mainFrame = new JFrame(APP_TITLE);
        mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        mainFrame.setSize(WIN_WIDTH, WIN_HEIGHT);
        mainFrame.setLocationRelativeTo(null);
        mainFrame.setLayout(new BorderLayout(5, 5));

        paramList = createParameterList();
        dataArea = createDataArea();
        statusLabel = new JLabel("Готов к работе.");
        dimensionFilter = createDimensionFilter();
        
        JSplitPane splitPane = new JSplitPane(JSplitPane.HORIZONTAL_SPLIT, 
                                              new JScrollPane(paramList), 
                                              new JScrollPane(dataArea));
        splitPane.setDividerLocation(DIVIDER_LOC);

        JPanel controlPanel = createControlPanel();

        mainFrame.add(splitPane, BorderLayout.CENTER);
        mainFrame.add(controlPanel, BorderLayout.SOUTH);
        mainFrame.add(dimensionFilter, BorderLayout.NORTH);
    }

    public void show() {
        mainFrame.setVisible(true);
    }

    private JComboBox<String> createDimensionFilter() {
        String[] dimensions = {
            "Все размерности",
            "B (Вольт)",
            "A (Ампер)",
            "M/CEK (м/с)",
            "KM/CEK (км/с)",
            "CM/CEK (см/с)",
            "M/CEK2 (м/с²)",
            "CEK (сек)",
            "MIN (мин)",
            "KPA (кПа)",
            "MPA (МПа)",
            "ATA (атм)",
            "KPA/CEK (кПа/с)",
            "K (Кельвин)",
            "C (Цельсий)",
            "KPA K (кПа·К)",
            "KG (кг)",
            "M (метр)",
            "MM (мм)",
            "CM (см)",
            "KM (км)",
            "M3 (м³)",
            "CM3 (см³)",
            "M3/CH (м³/ч)",
            "CM3/CEK (см³/с)",
            "OB/MIN (об/мин)",
            "1/CEK (Гц)",
            "G (g)",
            "H (Ньютон)",
            "BT (Ватт)",
            "MB (мВ)",
            "MA (мА)",
            "OM (Ом)",
            "KG/CM2 (кг/см²)",
            "KG/M2 (кг/м²)",
            "KG/CEK (кг/с)",
            "KG/SM3 (кг/см³)",
            "A/G (А/ч)",
            "B/G (В/ч)",
            "M/CH (м/ч)",
            "MM/CH (мм/ч)",
            "CM3/MIN (см³/мин)",
            "M3/MIN (м³/мин)",
            "% (процент)",
            "%O2 (O2 %)",
            "Без размерности"
        };
        
        JComboBox<String> combo = new JComboBox<>(dimensions);
        combo.setFont(new Font("SansSerif", Font.PLAIN, 16));
        combo.setPreferredSize(new Dimension(300, 35));
        combo.setMaximumRowCount(20);
        combo.addActionListener(e -> filterParametersByDimension());
        return combo;
    }

    private void filterParametersByDimension() {
        if (telemetryReader == null) return;
        
        String selectedDim = (String) dimensionFilter.getSelectedItem();
        listModel.clear();
        
        String dimPattern = extractDimPattern(selectedDim);
        
        for (String paramName : allParameters) {
            if (dimPattern == null || matchesDimension(paramName, dimPattern)) {
                listModel.addElement(paramName);
            }
        }
        
        statusLabel.setText(String.format("Показано параметров: %d (из %d)", 
            listModel.getSize(), allParameters.size()));
    }

    private String extractDimPattern(String selectedDim) {
        if (selectedDim == null || selectedDim.equals("Все размерности")) {
            return null;
        }
        if (selectedDim.startsWith("Без размерности")) {
            return "";
        }
        // Извлекаем код размерности из строки вида "B (Вольт)" → "B"
        int parenIndex = selectedDim.indexOf(" (");
        if (parenIndex > 0) {
            return selectedDim.substring(0, parenIndex).trim();
        }
        return selectedDim.trim();
    }

    private boolean matchesDimension(String paramName, String dimPattern) {
        if (telemetryReader == null) return false;
        
        for (TmDat record : telemetryReader.records) {
            if (paramName.equals(record.name)) {
                if (dimPattern.isEmpty()) {
                    return record.dimension == null || record.dimension.trim().isEmpty() 
                        || record.dimension.startsWith("dim=");
                }
                return record.dimension != null && record.dimension.contains(dimPattern);
            }
        }
        return false;
    }

    private JList<String> createParameterList() {
        JList<String> list = new JList<>(listModel);
        list.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        list.setFont(new Font("SansSerif", Font.BOLD, 22));
        list.addListSelectionListener(e -> {
            if (!e.getValueIsAdjusting()) {
                String selected = list.getSelectedValue();
                if (selected != null) displayParameterHistory(selected);
            }
        });
        return list;
    }

    private JTextArea createDataArea() {
        JTextArea area = new JTextArea();
        area.setEditable(false);
        area.setFont(new Font("Monospaced", Font.PLAIN, 20));
        return area;
    }

    private JPanel createControlPanel() {
        JPanel panel = new JPanel(new FlowLayout(FlowLayout.CENTER, 15, 10));

        JButton btnRun = new JButton("Перезапуск");
        JButton btnStats = new JButton("Статистика");
        JButton btnChart = new JButton("Диаграмма");
        
        btnRun.setFont(new Font("SansSerif", Font.BOLD, 20));
        btnStats.setFont(new Font("SansSerif", Font.BOLD, 20));
        btnChart.setFont(new Font("SansSerif", Font.BOLD, 20));

        btnRun.addActionListener(e -> startParsing());
        btnStats.addActionListener(e -> showStatisticsDialog());
        btnChart.addActionListener(e -> showChartDialog());

        panel.add(btnRun);
        panel.add(btnStats);
        panel.add(btnChart);
        
        statusLabel.setFont(new Font("SansSerif", Font.BOLD, 18));
        panel.add(statusLabel);

        return panel;
    }

    private void startParsing() {
        statusLabel.setText("Обработка данных...");
        dataArea.setText("");
        listModel.clear();

        new Thread(() -> {
            try {
                long startTime = System.currentTimeMillis();

                Dim dim = new Dim(FILE_DIM);
                DatXML xml = new DatXML(FILE_XML);
                telemetryReader = new ReadTMI(FILE_KNP, xml, dim);
                
                telemetryReader.load();

                long duration = System.currentTimeMillis() - startTime;
                updateUIOnSuccess(duration);

            } catch (Exception e) {
                updateUIOnError(e);
            }
        }).start();
    }

    private void displayParameterHistory(String paramName) {
        if (paramName == null || telemetryReader == null) return;

        List<TmDat> filtered = new ArrayList<>();
        int maxValLen = 10; 

        for (TmDat record : telemetryReader.records) {
            if (paramName.equals(record.name)) {
                filtered.add(record);
                int len = record.getValueString().length();
                if (len > maxValLen) maxValLen = len;
            }
        }

        StringBuilder report = new StringBuilder();
        report.append(String.format("ИСТОРИЯ: %s\n\n", paramName));
        
        String format = "%-15s | %-" + maxValLen + "s | %s\n";
        
        report.append(String.format(format, "ВРЕМЯ", "ЗНАЧЕНИЕ", "РАЗМЕРНОСТЬ"));
        
        String lineTime = new String(new char[15]).replace("\0", "-");
        String lineVal = new String(new char[maxValLen]).replace("\0", "-");
        String lineDim = new String(new char[15]).replace("\0", "-");
        
        report.append(String.format(format, lineTime, lineVal, lineDim));
        
        for (TmDat record : filtered) {
            report.append(String.format(format,
                    record.getTimeString(), 
                    record.getValueString(), 
                    record.dimension));
        }
        report.append("\n[Всего записей: ").append(filtered.size()).append("]");
        
        dataArea.setText(report.toString());
        dataArea.setCaretPosition(0);
    }

    /*private void showStatisticsDialog() {
        if (telemetryReader == null) {
            JOptionPane.showMessageDialog(mainFrame, "Нет данных для отображения.", "Внимание", JOptionPane.WARNING_MESSAGE);
            return;
        }

        JFrame dialog = new JFrame("Отчет статистики");
        dialog.setSize(900, 700);
        dialog.setLocationRelativeTo(mainFrame);
        dialog.setLayout(new BorderLayout());

        JTextArea statsText = new JTextArea(telemetryReader.stats.generateReport());
        statsText.setEditable(false);
        statsText.setFont(new Font("Monospaced", Font.PLAIN, 20));
        statsText.setCaretPosition(0);

        JButton closeBtn = new JButton("Закрыть");
        closeBtn.setFont(new Font("SansSerif", Font.BOLD, 20));
        closeBtn.addActionListener(e -> dialog.dispose());
        JPanel btnPanel = new JPanel();
        btnPanel.add(closeBtn);

        dialog.add(new JScrollPane(statsText), BorderLayout.CENTER);
        dialog.add(btnPanel, BorderLayout.SOUTH);
        dialog.setVisible(true);
    }*/
    private void showStatisticsDialog() {
        if (telemetryReader == null) return;

        JFrame dialog = new JFrame("Выбор вопросов статистики");
        dialog.setSize(1000, 700);
        dialog.setLocationRelativeTo(mainFrame);

        Map<String, String> questions = telemetryReader.stats.generateQuestionsMap();
        
        // Создаем список и модель
        DefaultListModel<String> listModel = new DefaultListModel<>();
        questions.keySet().forEach(listModel::addElement);
        
        JList<String> questionList = new JList<>(listModel);
        questionList.setFont(new Font("SansSerif", Font.PLAIN, 16));
        questionList.setSelectionMode(ListSelectionModel.MULTIPLE_INTERVAL_SELECTION);

        JTextArea display = new JTextArea();
        display.setFont(new Font("Monospaced", Font.PLAIN, 18));
        display.setEditable(false);
        display.setMargin(new Insets(10, 10, 10, 10));

        // Слушатель изменения выбора в списке
        questionList.addListSelectionListener(e -> {
            if (!e.getValueIsAdjusting()) {
                StringBuilder combinedText = new StringBuilder();
                for (String selectedKey : questionList.getSelectedValuesList()) {
                    combinedText.append("--- ").append(selectedKey).append(" ---\n");
                    combinedText.append(questions.get(selectedKey)).append("\n\n");
                }
                display.setText(combinedText.toString());
                display.setCaretPosition(0); // Прокрутка наверх при обновлении
            }
        });

        // Панель для списка (слева)
        JScrollPane listScroll = new JScrollPane(questionList);
        listScroll.setPreferredSize(new Dimension(300, 0));
        
        // Панель для текста (справа)
        JScrollPane textScroll = new JScrollPane(display);

        // Разделитель (SplitPane) для удобства
        JSplitPane splitPane = new JSplitPane(JSplitPane.HORIZONTAL_SPLIT, listScroll, textScroll);
        splitPane.setDividerLocation(300);

        // Подсказка сверху
        JLabel hintLabel = new JLabel(" Зажмите Ctrl или Shift, чтобы выбрать несколько вопросов");
        hintLabel.setFont(new Font("SansSerif", Font.ITALIC, 14));

        JButton closeBtn = new JButton("Закрыть");
        closeBtn.addActionListener(ev -> dialog.dispose());

        dialog.add(hintLabel, BorderLayout.NORTH);
        dialog.add(splitPane, BorderLayout.CENTER);
        dialog.add(closeBtn, BorderLayout.SOUTH);

        dialog.setVisible(true);
    }

    private void showChartDialog() {
        if (telemetryReader == null || paramList.getSelectedValue() == null) {
            JOptionPane.showMessageDialog(mainFrame, 
                "Выберите параметр из списка для отображения диаграммы.", 
                "Внимание", 
                JOptionPane.WARNING_MESSAGE);
            return;
        }

        String paramName = paramList.getSelectedValue();
        List<TmDat> filteredRecords = new ArrayList<>();
        
        for (TmDat record : telemetryReader.records) {
            if (paramName.equals(record.name) && 
                (record instanceof TmDouble || record instanceof TmLong)) {
                filteredRecords.add(record);
            }
        }
        
        if (filteredRecords.isEmpty()) {
            JOptionPane.showMessageDialog(mainFrame, 
                "Нет числовых данных для отображения диаграммы.\n" +
                "Диаграммы поддерживаются только для параметров типа Long и Double.", 
                "Внимание", 
                JOptionPane.WARNING_MESSAGE);
            return;
        }

        JDialog dialog = new JDialog(mainFrame, "Диаграмма: " + paramName, true);
        dialog.setLayout(new BorderLayout());
        
        ChartPanel chartPanel = new ChartPanel(paramName);
        chartPanel.setData(filteredRecords);
        
        JButton closeBtn = new JButton("Закрыть");
        closeBtn.setFont(new Font("SansSerif", Font.BOLD, 18));
        closeBtn.addActionListener(e -> dialog.dispose());
        
        JButton exportBtn = new JButton("Сохранить");
        exportBtn.setFont(new Font("SansSerif", Font.BOLD, 18));
        exportBtn.addActionListener(e -> exportChart(chartPanel, paramName));
        
        JPanel btnPanel = new JPanel();
        btnPanel.add(exportBtn);
        btnPanel.add(closeBtn);

        dialog.add(chartPanel, BorderLayout.CENTER);
        dialog.add(btnPanel, BorderLayout.SOUTH);
        dialog.pack();
        dialog.setLocationRelativeTo(mainFrame);
        dialog.setVisible(true);
    }

    private void exportChart(ChartPanel chartPanel, String paramName) {
        JFileChooser fileChooser = new JFileChooser();
        fileChooser.setSelectedFile(new java.io.File(paramName + "_chart.png"));
        int option = fileChooser.showSaveDialog(mainFrame);
        if (option == JFileChooser.APPROVE_OPTION) {
            try {
                java.awt.image.BufferedImage image = new java.awt.image.BufferedImage(
                    chartPanel.getWidth(), 
                    chartPanel.getHeight(), 
                    java.awt.image.BufferedImage.TYPE_INT_RGB);
                Graphics2D g2d = image.createGraphics();
                g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
                chartPanel.paint(g2d);
                g2d.dispose();
                javax.imageio.ImageIO.write(image, "png", fileChooser.getSelectedFile());
                JOptionPane.showMessageDialog(mainFrame, 
                    "Диаграмма сохранена в файл:\n" + fileChooser.getSelectedFile().getAbsolutePath(), 
                    "Успех", 
                    JOptionPane.INFORMATION_MESSAGE);
            } catch (Exception ex) {
                JOptionPane.showMessageDialog(mainFrame, 
                    "Ошибка сохранения: " + ex.getMessage(), 
                    "Ошибка", 
                    JOptionPane.ERROR_MESSAGE);
            }
        }
    }

    private void updateUIOnSuccess(long duration) {
        TreeSet<String> uniqueNames = new TreeSet<>();
        for (TmDat td : telemetryReader.records) {
            if (td.name != null) uniqueNames.add(td.name);
        }

        SwingUtilities.invokeLater(() -> {
            allParameters.clear();
            allParameters.addAll(uniqueNames);
            
            for (String name : uniqueNames) listModel.addElement(name);

            statusLabel.setText(String.format("Готово (%d мс). Записей: %,d", duration, telemetryReader.stats.S));
            dataArea.setText("--- ПАРСИНГ ЗАВЕРШЕН ---\n\n" +
                             telemetryReader.sessionInfo + "\n" +
                             "Режим: " + telemetryReader.stats.currentMode + "\n\n" +
                             "Выберите параметр из списка слева для просмотра данных.");
        });
    }

    private void updateUIOnError(Exception e) {
        SwingUtilities.invokeLater(() -> {
            statusLabel.setText("Произошла ошибка.");
            dataArea.setText("КРИТИЧЕСКАЯ ОШИБКА:\n" + e.toString());
            e.printStackTrace();
        });
    }
}