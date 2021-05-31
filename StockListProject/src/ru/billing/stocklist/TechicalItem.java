package ru.billing.stocklist;

public class TechicalItem extends GenericItem implements Cloneable {
    private Category category = Category.GENERAL;
    private short warrantyTime;

    @Override
    void printAll() {
        System.out.printf("ID: %d , Name: %-20s , price: %5.2f , category: %s , warranty time: %d \n",
                getID(), getName(), getPrice(), category, warrantyTime);
    }

    @Override
    public boolean equals(Object o) {
        if (!(o instanceof TechicalItem))
            return false;
        GenericItem obj = (TechicalItem) o;
        return this.getID() == obj.getID();
    }

    @Override
    public Object clone() throws CloneNotSupportedException {
        return super.clone();
    }

    @Override
    public String toString() {
        return "TechicalItem{"
                + "ID='" + getID() + '\''
                + ", Name=" + getName()
                + ", Price=" + getPrice()
                + ", Category=" + category
                + ", Category=" + warrantyTime
                + '}';
    }
}
