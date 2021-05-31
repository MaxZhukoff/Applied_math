package ru.billing.stocklist;

import java.util.Objects;

public class GenericItem implements Cloneable {
    private static int currentID = 0;
    private int ID;
    private String name;
    private float price;
    private GenericItem analog = null;
    private Category category = Category.GENERAL;

    public static int getCurrentID() {
        return currentID;
    }

    public static void setCurrentID(int currentID) {
        GenericItem.currentID = currentID;
    }

    public int getID() {
        return ID;
    }

    public void setID(int ID) {
        this.ID = ID;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }

    public GenericItem getAnalog() {
        return analog;
    }

    public void setAnalog(GenericItem analog) {
        this.analog = analog;
    }

    public Category getCategory() {
        return category;
    }

    public void setCategory(Category category) {
        this.category = category;
    }

    public GenericItem(String name, float price, Category category) {
        this.name = name;
        this.price = price;
        this.category = category;
        this.ID = GenericItem.currentID++;
    }

    public GenericItem(String name, float price, GenericItem analog) {
        this(name, price, Category.GENERAL);
        this.analog = analog;
    }

    public GenericItem() {
        this("", 0f, Category.GENERAL);
    }

    GenericItem addAnalogue(GenericItem analog) {
        if (analog != null) {
            this.analog = analog;
            this.analog.ID = GenericItem.currentID++;
        }
        return analog;
    }

    void printAnalogue() {
        if (analog != null)
            System.out.printf("Analogue:\nID: %d , Name: %-20s , price: %5.2f , category: %s \n", analog.ID,
                    analog.name, analog.price, analog.category);
    }

    void printAll() {
        System.out.printf("ID: %d , Name: %-20s , price: %5.2f , category: %s \n", ID, name, price, category);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        GenericItem that = (GenericItem) o;
        return ID == that.ID && Float.compare(that.price, price) == 0 && Objects.equals(name, that.name)
                && Objects.equals(analog, that.analog) && category == that.category;
    }

    public Object clone() throws CloneNotSupportedException {
        return super.clone();
    }

    public String toString() {
        return "GenericItem{"
                + "ID='" + ID + '\''
                + ", Name=" + name
                + ", Price=" + price
                + ", Category=" + category
                + '}';
    }
}