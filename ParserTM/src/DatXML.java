import javax.xml.parsers.*;
import org.xml.sax.*;
import org.xml.sax.helpers.DefaultHandler;
import java.io.*;
import java.util.TreeMap;

/**
 * SAX-парсер XML-файла с описанием параметров.
 * Извлекает name и number из вложенных элементов <Param>.
 * Результат: TreeMap<Integer, String> — (number → name).
 */
public class DatXML {
    public TreeMap<Integer, String> map = new TreeMap<>();

    public DatXML(String filename) {
        try {
            SAXParserFactory factory = SAXParserFactory.newInstance();
            SAXParser saxParser = factory.newSAXParser();

            DefaultHandler handler = new DefaultHandler() {
                @Override
                public void startElement(String uri, String localName,
                        String qName, Attributes attributes) {
                    if ("Param".equalsIgnoreCase(qName)) {
                        String name = attributes.getValue("name");
                        String numberStr = attributes.getValue("number");
                        if (name != null && numberStr != null) {
                            try {
                                int number = Integer.parseInt(numberStr);
                                map.put(number, name);
                            } catch (NumberFormatException e) {
                                // пропустить некорректные записи
                            }
                        }
                    }
                }
            };

            saxParser.parse(new File(filename), handler);
        } catch (Exception e) {
            System.out.println("Ошибка чтения XML: " + e.getMessage());
        }
    }

    public String getName(int id) {
        String s = map.get(id);
        return (s != null) ? s : "Unknown";
    }
}
