package com.company;

import java.sql.*;
import java.util.ArrayList;
import java.util.Collection;

import com.javatunes.util.ItemDAO;
import com.javatunes.util.MusicItem;

public class ItemDAOMain {
    public static void main(String[] args) throws ClassNotFoundException, SQLException {
        MusicItem musicItem = null;
        Connection conn = null;
        Class.forName("org.apache.derby.jdbc.ClientDriver");
        conn = DriverManager.getConnection("jdbc:derby://localhost:1527/JavaTunesDB", "GUEST", "1234");
        ItemDAO itemDAO = new ItemDAO(conn);

        System.out.println("ID 1:");
        musicItem = itemDAO.searchById(1L);
        if (musicItem != null) {
            System.out.println(musicItem.toString());
        }
        System.out.println("ID 100:");
        musicItem = itemDAO.searchById(100L);
        if (musicItem != null) {
            System.out.println(musicItem.toString());
        }

        System.out.println("of:");
        Collection<MusicItem> result2 = itemDAO.searchByKeyword("of");
        if (result2 != null) {
            for (MusicItem item: result2){
                System.out.println(item.toString());
            }
        }
        System.out.println("Gay:");
        result2 = itemDAO.searchByKeyword("Gay");
        if (result2 != null) {
            for (MusicItem item: result2){
                System.out.println(item.toString());
            }
        }

        musicItem = itemDAO.searchById(1L);
        System.out.println("Created:");
        itemDAO.create(musicItem);

        conn.close();
    }
}
