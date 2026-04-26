/*
 * =============================================================================
 * Класс: ChartPanel
 *
 * Назначение:
 * Панель для отрисовки графиков телеметрических параметров.
 * Поддерживает отображение числовых данных (Long, Double) в виде линейного графика.
 *
 * ---------------------------------------------------------------------------
 * 1. Поля класса
 *
 * dataPoints    (List<DataPoint>) – данные для графика (время, значение).
 * paramName     (String)          – имя отображаемого параметра.
 * maxValue      (double)          – максимальное значение на графике.
 * minValue      (double)          – минимальное значение на графике.
 *
 * =============================================================================
 */

import java.awt.*;
import java.util.*;
import javax.swing.*;

public class ChartPanel extends JPanel {
    
    private static final String CHART_TITLE_PREFIX = "График параметра";
    
    private static final int PADDING_TOP = 60;
    private static final int PADDING_BOTTOM = 50;
    private static final int PADDING_LEFT = 80;
    private static final int PADDING_RIGHT = 40;
    
    private static final Color GRID_COLOR = new Color(200, 200, 200);
    private static final Color LINE_COLOR = new Color(41, 98, 255);
    private static final Color TEXT_COLOR = Color.DARK_GRAY;
    private static final Color BACKGROUND_COLOR = Color.WHITE;
    
    private java.util.List<DataPoint> dataPoints;
    private String paramName;
    private double maxValue;
    private double minValue;
    private int maxTime;
    private int minTime;

    public ChartPanel(String paramName) {
        this.paramName = paramName;
        this.dataPoints = new ArrayList<>();
        this.maxValue = Double.NEGATIVE_INFINITY;
        this.minValue = Double.POSITIVE_INFINITY;
        this.maxTime = 0;
        this.minTime = Integer.MAX_VALUE;
        setBackground(BACKGROUND_COLOR);
        setPreferredSize(new Dimension(900, 600));
    }

    public void addDataPoint(long timeMs, double value) {
        dataPoints.add(new DataPoint(timeMs, value));
        if (value > maxValue) maxValue = value;
        if (value < minValue) minValue = value;
        if (timeMs > maxTime) maxTime = (int) timeMs;
        if (timeMs < minTime) minTime = (int) timeMs;
    }

    public void setData(java.util.List<TmDat> records) {
        dataPoints.clear();
        maxValue = Double.NEGATIVE_INFINITY;
        minValue = Double.POSITIVE_INFINITY;
        maxTime = 0;
        minTime = Integer.MAX_VALUE;
        
        for (TmDat record : records) {
            double value = parseValue(record);
            if (!Double.isNaN(value)) {
                dataPoints.add(new DataPoint(record.time, value));
                if (value > maxValue) maxValue = value;
                if (value < minValue) minValue = value;
                if (record.time > maxTime) maxTime = (int) record.time;
                if (record.time < minTime) minTime = (int) record.time;
            }
        }
        
        // Add 5% margin to min/max
        double range = maxValue - minValue;
        if (range > 0) {
            maxValue += range * 0.05;
            minValue -= range * 0.05;
        }
        
        repaint();
    }

    private double parseValue(TmDat record) {
        if (record instanceof TmDouble) {
            return ((TmDouble) record).value;
        } else if (record instanceof TmLong) {
            return (double) ((TmLong) record).value;
        }
        return Double.NaN;
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2d = (Graphics2D) g;
        g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
        
        int width = getWidth();
        int height = getHeight();
        
        // Draw background
        g2d.setColor(BACKGROUND_COLOR);
        g2d.fillRect(0, 0, width, height);
        
        // Draw border
        g2d.setColor(Color.BLACK);
        g2d.drawRect(0, 0, width - 1, height - 1);
        
        if (dataPoints.isEmpty()) {
            g2d.setColor(TEXT_COLOR);
            g2d.setFont(new Font("SansSerif", Font.PLAIN, 18));
            g2d.drawString("Нет данных для отображения", width / 2 - 150, height / 2);
            return;
        }
        
        int chartWidth = width - PADDING_LEFT - PADDING_RIGHT;
        int chartHeight = height - PADDING_TOP - PADDING_BOTTOM;
        
        // Draw grid
        drawGrid(g2d, PADDING_LEFT, PADDING_TOP, chartWidth, chartHeight);
        
        // Draw axes
        drawAxes(g2d, PADDING_LEFT, PADDING_TOP, chartWidth, chartHeight);
        
        // Draw data line
        drawDataLine(g2d, PADDING_LEFT, PADDING_TOP, chartWidth, chartHeight);
        
        // Draw title
        drawTitle(g2d, width);
        
        // Draw legend
        drawLegend(g2d, width, height);
    }

    private void drawGrid(Graphics2D g2d, int x, int y, int w, int h) {
        g2d.setColor(GRID_COLOR);
        g2d.setStroke(new BasicStroke(1));
        
        // Horizontal grid lines (5 lines)
        for (int i = 0; i <= 5; i++) {
            int gy = y + (h * i / 5);
            g2d.drawLine(x, gy, x + w, gy);
        }
        
        // Vertical grid lines (10 lines)
        for (int i = 0; i <= 10; i++) {
            int gx = x + (w * i / 10);
            g2d.drawLine(gx, y, gx, y + h);
        }
    }

    private void drawAxes(Graphics2D g2d, int x, int y, int w, int h) {
        g2d.setColor(Color.BLACK);
        g2d.setStroke(new BasicStroke(2));
        
        // Y-axis
        g2d.drawLine(x, y, x, y + h);
        
        // X-axis
        g2d.drawLine(x, y + h, x + w, y + h);
        
        // Y-axis labels
        g2d.setColor(TEXT_COLOR);
        g2d.setFont(new Font("SansSerif", Font.PLAIN, 14));
        FontMetrics fm = g2d.getFontMetrics();
        
        for (int i = 0; i <= 5; i++) {
            int gy = y + (h * i / 5);
            double value = maxValue - (maxValue - minValue) * i / 5;
            String label = formatValue(value);
            int labelWidth = fm.stringWidth(label);
            g2d.drawString(label, x - labelWidth - 10, gy + 5);
        }
        
        // X-axis labels (time)
        int timeRange = maxTime - minTime;
        for (int i = 0; i <= 10; i++) {
            int gx = x + (w * i / 10);
            int timeMs = minTime + (timeRange * i / 10);
            String label = formatTime(timeMs);
            int labelWidth = fm.stringWidth(label);
            g2d.drawString(label, gx - labelWidth / 2, y + h + 25);
        }
        
        // Axis titles
        g2d.setFont(new Font("SansSerif", Font.BOLD, 14));
        g2d.drawString("Значение", x - 70, y + h / 2);
        g2d.drawString("Время", x + w / 2 - 30, y + h + 45);
    }

    private void drawDataLine(Graphics2D g2d, int x, int y, int w, int h) {
        g2d.setColor(LINE_COLOR);
        g2d.setStroke(new BasicStroke(3, BasicStroke.CAP_ROUND, BasicStroke.JOIN_ROUND, 0));
        
        int[] xPoints = new int[dataPoints.size()];
        int[] yPoints = new int[dataPoints.size()];
        
        double range = maxValue - minValue;
        if (range == 0) range = 1;
        
        int timeRange = maxTime - minTime;
        if (timeRange == 0) timeRange = 1;
        
        for (int i = 0; i < dataPoints.size(); i++) {
            DataPoint dp = dataPoints.get(i);
            xPoints[i] = x + (int) (((dp.time - minTime) / (double) timeRange) * w);
            yPoints[i] = y + h - (int) (((dp.value - minValue) / range) * h);
        }
        
        if (dataPoints.size() > 1) {
            g2d.drawPolyline(xPoints, yPoints, dataPoints.size());
        }
        
        // Draw data points
        g2d.setColor(LINE_COLOR.brighter());
        g2d.setStroke(new BasicStroke(2));
        for (int i = 0; i < xPoints.length; i++) {
            g2d.fillOval(xPoints[i] - 4, yPoints[i] - 4, 8, 8);
        }
    }

    private void drawTitle(Graphics2D g2d, int width) {
        g2d.setColor(Color.BLACK);
        g2d.setFont(new Font("SansSerif", Font.BOLD, 20));
        FontMetrics fm = g2d.getFontMetrics();
        String title = CHART_TITLE_PREFIX + ": " + paramName;
        int titleWidth = fm.stringWidth(title);
        g2d.drawString(title, width / 2 - titleWidth / 2, 30);
    }

    private void drawLegend(Graphics2D g2d, int width, int height) {
        g2d.setColor(LINE_COLOR);
        g2d.setStroke(new BasicStroke(3));
        int legendX = width - 200;
        int legendY = height - 30;
        
        g2d.drawLine(legendX, legendY, legendX + 30, legendY);
        
        g2d.setColor(Color.BLACK);
        g2d.setFont(new Font("SansSerif", Font.PLAIN, 14));
        g2d.drawString("Значения", legendX + 40, legendY + 5);
        
        // Show min/max values
        g2d.drawString(String.format("Min: %s", formatValue(minValue)), legendX, height - 50);
        g2d.drawString(String.format("Max: %s", formatValue(maxValue)), legendX, height - 35);
    }

    private String formatValue(double value) {
        if (Math.abs(value) >= 1000 || (Math.abs(value) < 0.01 && value != 0)) {
            return String.format("%.2e", value);
        } else if (value == (int) value) {
            return String.format("%d", (int) value);
        } else {
            return String.format("%.2f", value);
        }
    }

    private String formatTime(int timeMs) {
        long hours = timeMs / 3600000;
        long minutes = (timeMs % 3600000) / 60000;
        long seconds = (timeMs % 60000) / 1000;
        return String.format("%02d:%02d:%02d", hours, minutes, seconds);
    }

    public boolean hasData() {
        return !dataPoints.isEmpty();
    }

    private static class DataPoint {
        long time;
        double value;
        
        DataPoint(long time, double value) {
            this.time = time;
            this.value = value;
        }
    }
}
