package com.intellihealthapp.main.controller;

import com.fasterxml.jackson.core.JsonProcessingException;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.List;
@Slf4j
@Controller
public class MainChat {
    @RequestMapping(value = "/chat/{content}", method = RequestMethod.GET, produces = MediaType.APPLICATION_JSON_VALUE)
    @ResponseBody
    public String getResponses(@PathVariable(value="content") String content) throws JsonProcessingException{
        System.out.println(content);
        return "hello world";
    }

    @RequestMapping("/test")
    @ResponseBody
    public String dummyMessage() {
        return "hello world";
    }
}
