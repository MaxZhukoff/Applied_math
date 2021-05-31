package ru.billing.stocklist;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class ItemCatalog {
    private Map<Integer, GenericItem> catalog = new HashMap<>();
    private List<GenericItem> ALCatalog = new ArrayList<>();

    public void addItem(GenericItem item) {
        catalog.put(item.getID(), item); // Добавляем товар в HashMap
        ALCatalog.add(item); // Добавляем тот же товар в ArrayList
    }

    public void printItems() {
        for (GenericItem i : ALCatalog) {
            System.out.println(i);
        }
    }

    public GenericItem findItemByID(int id) {
        return catalog.getOrDefault(id, null); //Если нет такого ID, возвращаем пустое значение
    }

    public GenericItem findItemByIDAL(int id) {
        for (GenericItem i : ALCatalog) {
            if (i.getID() == id) {
                return i;
            }
        }
        return null;
    }
}

