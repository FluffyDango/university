package com.kasbus.kasbusapp.Containers;

import com.google.gson.annotations.SerializedName;

public class Ratings {
    @SerializedName("category1")
    private Double category1;   // Interest
    @SerializedName("category2")
    private Double category2;   // Amount of work
    @SerializedName("category3")
    private Double category3;   // Actuality
    @SerializedName("category4")
    private Double category4;   // Teaching

    public Double getCategory1(){
        return category1;
    }

//    public void setCategory1(Double newCategory1){
//        this.category1 = newCategory1;
//    }
    
    public Double getCategory2(){
        return category2;
    }

//    public void setCategory2(Double newCategory2){
//        this.category2 = newCategory2;
//    }

    public Double getCategory3(){
        return category3;
    }

//    public void setCategory3(Double newCategory3){
//        this.category3 = newCategory3;
//    }

    public Double getCategory4(){
        return category4;
    }

//    public void setCategory4(Double newCategory4){
//        this.category4 = newCategory4;
//    }
}
