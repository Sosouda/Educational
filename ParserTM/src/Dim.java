import java.io.*;
import java.util.HashMap;

public class Dim {
    public HashMap<Integer, String> map = new HashMap<>();

    public Dim(String filename) {
        // Change UTF-8 to Cp1251 (Windows-1251) for Russian text support
        try (BufferedReader br = new BufferedReader(
                new InputStreamReader(new FileInputStream(filename), "Cp1251"))) {
            String line;
            int code = 1;
            while ((line = br.readLine()) != null) {
                map.put(code, line.trim());
                code++;
            }
        } catch (Exception e) {
            System.out.println("Error reading dimens.ion: " + e.getMessage());
        }
    }

    public String get(int code) {
        String s = map.get(code);
        return (s != null) ? s : ("dim=" + code);
    }
}