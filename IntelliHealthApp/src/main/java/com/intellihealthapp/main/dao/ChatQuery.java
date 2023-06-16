package com.intellihealthapp.main.dao;

import com.intellihealthapp.main.utils.RequestsGenerator;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;


@Repository
public class ChatQuery {

    @Autowired
    RequestsGenerator generator;

    public String queryChat(String content) {
        String response = generator.generateChat(content);
        System.out.println("ChatQuery: " + response);
        return response;
    }
}
