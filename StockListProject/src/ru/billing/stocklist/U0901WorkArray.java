package ru.billing.stocklist;

public class U0901WorkArray<T extends Number> {
    T[] arrNums;

    public U0901WorkArray(T[] numP) {
        arrNums = numP;
    }

    double sum() {
        double doubleWork = 0;
        for (T arrNum : arrNums) {
            doubleWork += arrNum.doubleValue();
        }
        return doubleWork;
    }

    public static class U0901Main {
        public static void main(String[] args) {
            Integer intArr[] = {10, 20, 15};
            Float[] floatArr = new Float[3];
            for (int i = 0; i < floatArr.length; i++) {
                floatArr[i] = 10.1F;
                floatArr[i] = 20.1F;
                floatArr[i] = 15.1F;
//                floatArr[i] = (float) Math.random() * 100;
//                System.out.println(floatArr[i]);
            }
            U0901WorkArray<Integer> insWorkArrayInt = new U0901WorkArray<>(intArr);
            U0901WorkArray<Float> insWorkArrayFloat = new U0901WorkArray<>(floatArr);
            System.out.println((int) insWorkArrayInt.sum());
            System.out.printf("%.1f\n", (float) insWorkArrayFloat.sum());
//            String[] stringArr = {"raz", "dva", "tri"};
//            U0901WorkArray<String> insWorkArrayString = new U0901WorkArray<>(floatArr);
        }
    }
}
