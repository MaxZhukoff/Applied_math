package ru.billing.client;

import ru.billing.stocklist.GenericItem;
import ru.billing.stocklist.ItemCatalog;

import java.util.ArrayList;

public class CatalogStubLoader implements CatalogLoader {
    @Override
    public void load(ItemCatalog cat, ArrayList<GenericItem> list) {
        for (GenericItem i : list) {
            cat.addItem(i);;
        }
    }
}
