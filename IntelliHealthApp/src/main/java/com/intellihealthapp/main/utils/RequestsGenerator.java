package com.intellihealthapp.main.utils;
//import okhttp3.;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.client.RestTemplate;

public class RequestsGenerator {
    private static final String OPENAI_URL = "https://api.openai.com/v1/chat/completions";
    private static final String apiKey = "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";
    private final RestTemplate restTemplate = new RestTemplate();

    public String generateChat(String prompt) {
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);
        headers.set("Authorization", "Bearer " + apiKey);
        String modelId = "gpt-3.5-turbo";

//        String requestJson = "{\n" +
//                "  \"model\": \"gpt-3.5-turbo\",\n" +
//                "  \"input\": \"" + prompt + "\",\n" +
//                "}";
        String requestJson = "{\"model\": \"" + modelId + "\", \"messages\": [{\"role\": \"system\", \"content\": \"You are a helpful assistant.\"}, {\"role\": \"user\", \"content\": \"" + prompt + "\"}]}";

        HttpEntity<String> request = new HttpEntity<>(requestJson, headers);
        ResponseEntity<String> response = restTemplate.postForEntity(OPENAI_URL, request, String.class);
        return response.getBody();
    }
}
