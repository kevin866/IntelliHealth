package com.intellihealthapp.main.controller;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.intellihealthapp.main.service.ChatService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.List;

@Slf4j
@Controller
public class ChatController {

    @Autowired
    private ChatService chatService;

    @RequestMapping(value = "/chat/{content}", method = RequestMethod.GET, produces = MediaType.APPLICATION_JSON_VALUE)
    @ResponseBody
    public String getResponses(@PathVariable(value="content") String content) throws IOException {
//        System.out.println(content);
        String decoded = java.net.URLDecoder.decode(content, StandardCharsets.UTF_8);
        System.out.println("Current input chat is: " + decoded);
        String chatResponse = chatService.getChatResponse(decoded);
        return chatResponse;
    }

    @RequestMapping("/test")
    @ResponseBody
    public String dummyMessage() {
        return "hello world";
    }
}
