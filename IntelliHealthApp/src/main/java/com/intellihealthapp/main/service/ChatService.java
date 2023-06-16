package com.intellihealthapp.main.service;

import com.intellihealthapp.main.dao.ChatQuery;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class ChatService {

    @Autowired
    private ChatQuery chatQuery;

    public String getChatResponse(String content) {
        String response = chatQuery.queryChat(content);
        return response;
    }
}
