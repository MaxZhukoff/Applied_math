package ru.billing.client;

import ru.billing.stocklist.GenericItem;
import ru.billing.stocklist.ItemCatalog;

import java.util.ArrayList;

public interface CatalogLoader {
    public void load(ItemCatalog cat, ArrayList<GenericItem> list);
}
