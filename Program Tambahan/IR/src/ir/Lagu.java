/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ir;

/**
 *
 * @author pasca
 */
public class Lagu {
    private String judul;
    private String lirik;
    private String penyanyi;

    public Lagu(String judul, String lirik, String penyanyi) {
        this.judul = judul;
        this.lirik = lirik;
        this.penyanyi = penyanyi;
    }

    public void setJudul(String judul) {
        this.judul = judul;
    }

    public void setLirik(String lirik) {
        this.lirik = lirik;
    }

    public String getJudul() {
        return judul;
    }

    public String getLirik() {
        return lirik;
    }

    public String getPenyanyi() {
        return penyanyi;
    }

    public void setPenyanyi(String penyanyi) {
        this.penyanyi = penyanyi;
    }

    
    
    public String toString(){
    return "Judul: "+judul+" Artis : "+penyanyi+" Lirik: "+lirik;
    }
}
