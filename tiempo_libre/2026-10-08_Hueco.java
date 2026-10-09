import java.util.*;
import java.time.*;
import java.time.chrono.*;

/** Hueco.java — qué cree la máquina que pasó en octubre de 1582 y de 1584.
 *  Uso: java Hueco.java   (Java 11 o posterior, sin compilar aparte) */
public class Hueco {
    static final String[] D = {"", "domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"};
    static String f(GregorianCalendar c) {
        return c.get(Calendar.DAY_OF_MONTH) + "/" + (c.get(Calendar.MONTH) + 1) + "/" + c.get(Calendar.YEAR) + " " + D[c.get(Calendar.DAY_OF_WEEK)];
    }
    public static void main(String[] a) {
        TimeZone utc = TimeZone.getTimeZone("UTC");
        GregorianCalendar c = new GregorianCalendar(utc);
        System.out.println("corte de java.util.GregorianCalendar: " + c.getGregorianChange().toInstant());
        System.out.println("-- le pido cada día de octubre de 1582 y me devuelve:");
        StringBuilder sb = new StringBuilder();
        for (int d = 1; d <= 18; d++) {
            c.clear(); c.setLenient(true); c.set(1582, Calendar.OCTOBER, d);
            sb.append(d).append("->").append(c.get(Calendar.DAY_OF_MONTH)).append(" ");
        }
        System.out.println(sb);
        c.clear(); c.set(1582, Calendar.OCTOBER, 8);
        System.out.println("8/10/1582 (permisivo): " + f(c));
        c.clear(); c.setLenient(false); c.set(1582, Calendar.OCTOBER, 8);
        try { c.getTime(); System.out.println("8/10/1582 (estricto): " + f(c)); }
        catch (Exception e) { System.out.println("8/10/1582 (estricto): " + e); }
        c.clear(); c.setLenient(true); c.set(1582, Calendar.OCTOBER, 1);
        System.out.println("días de octubre de 1582: máximo real " + c.getActualMaximum(Calendar.DAY_OF_MONTH)
            + " | 4 -> siguiente: ");
        c.clear(); c.set(1582, Calendar.OCTOBER, 4); String antes = f(c); c.add(Calendar.DAY_OF_MONTH, 1);
        System.out.println("   " + antes + "  ->  " + f(c));
        System.out.println("-- octubre de 1584, Córdoba (para Java ya es gregoriano):");
        c.clear(); c.set(1584, Calendar.OCTOBER, 8); System.out.println("8/10/1584: " + f(c));
        c.clear(); c.set(1580, Calendar.JUNE, 11); System.out.println("11/6/1580: " + f(c) + "  (antes del corte: lo toma por juliano)");
        c.clear(); c.set(1492, Calendar.OCTOBER, 12); System.out.println("12/10/1492: " + f(c));
        // el corte se puede mover: un calendario "cordobés"
        GregorianCalendar cba = new GregorianCalendar(utc);
        GregorianCalendar corte = new GregorianCalendar(utc); corte.clear(); corte.set(1585, Calendar.JUNE, 1);
        cba.setGregorianChange(corte.getTime());
        cba.clear(); cba.set(1584, Calendar.OCTOBER, 8); System.out.println("con el corte corrido a 1585, 8/10/1584: " + f(cba));
        cba.clear(); cba.set(1585, Calendar.JANUARY, 1); System.out.println("con el corte corrido a 1585, 1/1/1585: " + f(cba));
        System.out.println("-- java.time (ISO, gregoriano proléptico, sin hueco):");
        System.out.println("8/10/1582: " + LocalDate.of(1582, 10, 8).getDayOfWeek() + " | 8/10/1584: " + LocalDate.of(1584, 10, 8).getDayOfWeek()
            + " | 11/6/1580: " + LocalDate.of(1580, 6, 11).getDayOfWeek());
    }
}
