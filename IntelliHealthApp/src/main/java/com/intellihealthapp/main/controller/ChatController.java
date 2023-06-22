package com.intellihealthapp.main.controller;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.intellihealthapp.main.service.ChatService;
import lombok.extern.slf4j.Slf4j;
import net.razorvine.pickle.PickleException;
import net.razorvine.pickle.Unpickler;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.util.List;
import java.util.Map;

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
        InputStream fis = null;
        try {
            fis = new FileInputStream("src/main/java/com/intellihealthapp/main/utils/model.pkl");
            System.out.println(fis);
            Unpickler unpickler = new Unpickler();
//            Object model = unpickler.load(fis);
            Map<String, Object> model = (Map<String, Object>)unpickler.load(fis);
            System.out.println(model);
        } catch (IOException | PickleException e) {
            // Handle exceptions
            e.printStackTrace();
        } finally {
            if (fis != null) {
                try {
                    fis.close();
                } catch (IOException e) {
                    // Handle exceptions
                    e.printStackTrace();
                }
            }
        }
        return "hello world";
    }
}
