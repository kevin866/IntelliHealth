package com.intellihealthapp.main.utils;

import org.deeplearning4j.nn.modelimport.keras.KerasModelImport;
import org.deeplearning4j.nn.modelimport.keras.exceptions.InvalidKerasConfigurationException;
import org.deeplearning4j.nn.modelimport.keras.exceptions.UnsupportedKerasConfigurationException;
import org.deeplearning4j.nn.multilayer.MultiLayerNetwork;
import org.nd4j.common.io.ClassPathResource;
import org.nd4j.linalg.api.ndarray.INDArray;
import org.nd4j.linalg.factory.Nd4j;

import java.io.File;
import java.io.IOException;

public class ModelGenerator {
    private final String hdf5FilePath = "src/main/java/com/intellihealthapp/main/utils/data/model.h5";
    public ModelGenerator() throws IOException, UnsupportedKerasConfigurationException, InvalidKerasConfigurationException {
        // load the model
        String simpleMlp = new ClassPathResource("model.h5").getFile().getPath();
//        String simpleMlp =  hdf5FilePath;
//        File h5File = new File(simpleMlp);
//        MultiLayerNetwork model = KerasModelImport.importKerasSequentialModelAndWeights(simpleMlp, false);
//        // make a random sample
//        int inputs = 10;
//        INDArray features = Nd4j.zeros(inputs);
//        for (int i=0; i<inputs; i++)
//            features.putScalar(new int[] {i}, Math.random() < 0.5 ? 0 : 1);
//        double prediction = model.output(features).getDouble(0);
    }
}
