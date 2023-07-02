package com.intellihealthapp.main;

import com.intellihealthapp.main.utils.ModelGenerator;
import com.intellihealthapp.main.utils.RequestsGenerator;
import org.deeplearning4j.nn.modelimport.keras.exceptions.InvalidKerasConfigurationException;
import org.deeplearning4j.nn.modelimport.keras.exceptions.UnsupportedKerasConfigurationException;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;

import java.io.IOException;

@Configuration
@EnableWebMvc
public class IntelliHealthAppApplicationConfig {
    @Bean(name = "generator")
    public RequestsGenerator newGenerator() {
        RequestsGenerator generator = new RequestsGenerator();
        return generator;
    }

    @Bean(name = "model")
    public ModelGenerator newModelGenerator() throws IOException, UnsupportedKerasConfigurationException, InvalidKerasConfigurationException {
        ModelGenerator model = new ModelGenerator();
        return model;
    }
}
