package ru.billing.stocklist;

import java.util.Date;

public class FoodItem extends GenericItem implements Cloneable {
    private Category category = Category.FOOD;
    private Date dateOfIncome = new Date();
    private short expires;

    public FoodItem(String name, float price, short expires, FoodItem analog, Date date) {
        super(name, price, Category.FOOD);
        super.addAnalogue(analog);
        this.dateOfIncome = date;
        this.expires = expires;
    }

    public FoodItem(String name, float price, short expires) {
        this(name, price, expires, null, new Date());
    }

    public FoodItem(String name) {
        this(name, 0.0f, (short) 0, null, new Date());
    }

    @Override
    void printAll() {
        System.out.printf("ID: %d , Name: %-20s , price: %5.2f , category: %s , date Of income: '%Tc', expires: %d \n",
                getID(), getName(), getPrice(), category, dateOfIncome, expires);
    }

    @Override
    public boolean equals(Object o) {
        if (!(o instanceof FoodItem))
            return false;
        GenericItem obj = (FoodItem) o;
        return this.getID() == obj.getID();
    }

    @Override
    public Object clone() throws CloneNotSupportedException {
        return super.clone();
    }

    @Override
    public String toString() {
        return "FoodItem{"
                + "ID='" + getID() + '\''
                + ", Name=" + getName()
                + ", Price=" + getPrice()
                + ", Category=" + category
                + ", Date of income=" + dateOfIncome.toString()
                + ", Expires=" + expires
                + '}';
    }
}
