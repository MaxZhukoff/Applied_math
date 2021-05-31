package ru.billing.client;

import ru.billing.stocklist.FoodItem;
import ru.billing.stocklist.GenericItem;
import ru.billing.stocklist.ItemCatalog;

import java.util.Date;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        //4-1
        FoodItem milk = new FoodItem("milk", 80, (short) 7);
        FoodItem bread = new FoodItem("bead", 40, (short) 7);
        FoodItem water = new FoodItem("water", 50, (short) 360);
        FoodItem eggs = new FoodItem("eggs", 120, (short) 12);
        FoodItem cheese = new FoodItem("cheese", 580, (short) 15);
        FoodItem bacon = new FoodItem("bacon", 390, (short) 31);
        FoodItem cucumbers = new FoodItem("cucumbers", 40, (short) 31);
        FoodItem tomato = new FoodItem("tomato", 70, (short) 31);
        FoodItem crisps = new FoodItem("crisps", 120, (short) 180);
        FoodItem juice = new FoodItem("juice", 220, (short) 31);

        ItemCatalog itemCatalog = new ItemCatalog();
        itemCatalog.addItem(milk);
        itemCatalog.addItem(bread);
        itemCatalog.addItem(water);
        itemCatalog.addItem(eggs);
        itemCatalog.addItem(cheese);
        itemCatalog.addItem(bacon);
        itemCatalog.addItem(cucumbers);
        itemCatalog.addItem(tomato);
        itemCatalog.addItem(crisps);
        itemCatalog.addItem(juice);

        long begin = new Date().getTime();
        for (int i = 0; i < 100000; i++) {
            itemCatalog.findItemByID(9);
        }
        long end = new Date().getTime();
        System.out.println("In HashMap: " + (end - begin));
        begin = new Date().getTime();
        for (int i = 0; i < 100000; i++) {
            itemCatalog.findItemByIDAL(9);
        }
        end = new Date().getTime();
        System.out.println("In ArrayList: " + (end - begin));

        //4-2
        ArrayList<GenericItem> list = new ArrayList<GenericItem>();
        list.add(milk);
        list.add(bread);
        ItemCatalog cat = new ItemCatalog();
        CatalogLoader loader = new CatalogStubLoader();
        loader.load(cat, list);
        cat.printItems();

//        //3
//        String line = "Конфеты ’Маска’;45;120";
//        String[] item_fld;
//        item_fld = line.split(";");
//        try {
//            FoodItem item = new FoodItem(item_fld[0], Float.parseFloat(item_fld[1]), Short.parseShort(item_fld[2]));
//            item.printAll();
//        } catch (Exception e) {
//            e.printStackTrace();
//        }
//
//        //1-2
//        GenericItem bigMac = new GenericItem();
//        bigMac.name = "bigMac";
//        bigMac.price = 135;
//        bigMac.printAll();
//        GenericItem cheeseburger = new GenericItem();
//        cheeseburger.name = "cheeseburger";
//        cheeseburger.price = 52;
//        cheeseburger.printAll();
//        GenericItem chickenBurger = new GenericItem();
//        chickenBurger.name = "chickenBurger";
//        chickenBurger.price = 41;
//        chickenBurger.printAll();
//
//        GenericItem hamburger = new GenericItem();
//        hamburger.name = "hamburger";
//        hamburger.price = 50;
//        hamburger.printAll();
//        cheeseburger.addAnalogue(hamburger);
//        cheeseburger.printAnalogue();
//
//        System.out.println();
//        FoodItem apple = new FoodItem("apple");
//        apple.price = 10;
//        apple.expires = 31;
//        TechicalItem laptop = new TechicalItem();
//        laptop.name = "laptop";
//        laptop.price = 1000;
//        laptop.warrantyTime = 15;
//
//        GenericItem[] genericItems = new GenericItem[2];
//        genericItems[0] = apple;
//        genericItems[1] = laptop;
//        for (GenericItem genericItem : genericItems) {
//            genericItem.printAll();
//        }
//
//        System.out.println();
//        FoodItem milk = new FoodItem("milk");
//        milk.price = 70;
//        milk.expires = 7;
//        System.out.println(milk.equals(apple));
//
//        System.out.println();
//        try {
//            FoodItem cloneMild = (FoodItem) milk.clone();
//            System.out.println(cloneMild.equals(milk));
//        } catch (CloneNotSupportedException e) {
//            e.printStackTrace();
//        }
//
//        System.out.println();
//        System.out.println(hamburger.toString());
//        System.out.println(milk);
//
//        System.out.println();
//        System.out.println(cheeseburger.analog.name);
//        try {
//            GenericItem cloneCheeseburger = (GenericItem) cheeseburger.clone();
//            cloneCheeseburger.printAnalogue();
//        } catch (CloneNotSupportedException e) {
//            e.printStackTrace();
//        }
    }
}
