package com.intellihealthapp.main.dao;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import java.sql.Connection;
import java.util.ArrayList;
import java.util.List;

@Repository
public class ChatQuery {
//    @Autowired
//    Connection connection;

    public String queryChat(String content) {
        System.out.println(content);
        return "hello world";
    }
}
