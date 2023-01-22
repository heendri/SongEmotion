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
public class Label {
    private String judul;
    private String penyanyi;
    private String lirik;
    private String label;

    public Label(String judul, String penyanyi, String lirik, String label) {
        this.judul = judul;
        this.penyanyi = penyanyi;
        this.lirik = lirik;
        this.label = label;
    }

    public String getJudul() {
        return judul;
    }

    public String getPenyanyi() {
        return penyanyi;
    }

    public String getLirik() {
        return lirik;
    }

    public String getLabel() {
        return label;
    }

    public void setJudul(String judul) {
        this.judul = judul;
    }

    public void setPenyanyi(String penyanyi) {
        this.penyanyi = penyanyi;
    }

    public void setLirik(String lirik) {
        this.lirik = lirik;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    
}
