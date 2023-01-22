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
public class Emotion {
    private String token;
    private String emot;

    public Emotion(String token, String emot) {
        this.token = token;
        this.emot = emot;
    }

    public String getToken() {
        return token;
    }

    public String getEmot() {
        return emot;
    }

    public void setToken(String token) {
        this.token = token;
    }

    public void setEmot(String emot) {
        this.emot = emot;
    }
    
}
