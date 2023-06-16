package com.intellihealthapp.main.service;

import com.intellihealthapp.main.dao.ChatQuery;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ChatService {

    @Autowired
    private ChatQuery chatQuery;

    // get cart by id from cartDao
    public String getChatResponse(String content) {
        return chatQuery.queryChat(content);
    }
}
