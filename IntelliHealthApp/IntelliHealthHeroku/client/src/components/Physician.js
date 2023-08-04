

// import React, { useState } from 'react';
// import '../styles/SelectionButton.css'; 

// const SelectionButton = () => {
// const [isSelected1, setIsSelected1] = useState(false);
// const [isSelected2, setIsSelected2] = useState(false);

// const handleClick1 = () => {
// setIsSelected1(!isSelected1);
// };
// const handleClick2 = () => {
// setIsSelected2(!isSelected2);
// };

//   return (
//     <div>
//         <button
//             onClick={handleClick1}
//             className={`selection-button ${isSelected1 ? 'selected' : ''}`}
//             >
//             {isSelected1 ? 'Male' : 'Male'}
//         </button>
//         <button
//             onClick={handleClick2}
//             className={`selection-button ${isSelected2 ? 'selected' : ''}`}
//             >
//             {isSelected2 ? 'Female' : 'Female'}
//         </button>

//     </div>
    
//   );
// };

// export default SelectionButton;




import React, { Component } from 'react';
import { Button, Input, Card, Form, InputNumber, Tabs, Col, Row} from 'antd';
import axios from 'axios';
import SelectionButton from './SelectionButton'; // Import the SelectionButton component
import LoadingSpinner from "./LoadingSpinner";




const ASK_QUETIONS_URL = 'https://intellihealth-d355d13bbdb9.herokuapp.com/api/v1/chat/'
const QUOTE_MODEL_URL = 'https://intellihealth-d355d13bbdb9.herokuapp.com/api/v1/model/prediction'
const { TextArea } = Input;
let text1 = "sea";
class Physician extends Component {
    constructor(props) {
        super(props);
        // define state for the components states
        this.state = {
            currentQuestion: null,
            currentQuote: null,
            currentAnswer: "Your answer will be displayed here",
            gender: 0,
            age: 80,
            hypertension: 0,
            heartdisease: 1,
            smokingHistory: 4,
            bmi: 25.19,
            hbA1cLevel: 6.6,
            bloodGlucoseLevel: 140,
            currentPrediction: "Your prediction will be displayed here",
            maleisSelected1: false,
            femaleisSelected2: false,
            hyperisSelected1: false,
            hyperisSelected2: false,
            hedisisSelected1:false,
            hedisisSelected2:false,
            isLoading: false,
            setIsLoading:false,
        }
        this.formRef = React.createRef();
    }


    onClickExample1 = async () => {
        console.log("clicked example 1");
        await this.setState((prevState) => ({
            maleisSelected1: !prevState.maleisSelected1,
            gender: 0,
        }));
        await this.setState((prevState) => ({
            currentPrediction: "Your prediction will be displayed here",
        }));
        this.formRef.current.setFieldsValue({
            gender: 0,
        });
        if (this.state.femaleisSelected2) {
            await this.setState((prevState) => ({
                femaleisSelected2: !prevState.femaleisSelected2,
            }));
        }
        if (this.state.hedisisSelected2) {
            await this.setState((prevState) => ({
                hedisisSelected2: !prevState.hedisisSelected2,
            }));
        }
        if (this.state.hyperisSelected2) {
            await this.setState((prevState) => ({
                hyperisSelected2: !prevState.hyperisSelected2,
            }));
        }
        await this.setState({ age: 80 });
        this.formRef.current.setFieldsValue({
            age: 80,
        });
        await this.setState((prevState) => ({
            hyperisSelected1: !prevState.hyperisSelected1,
            hypertension: 0,
        }));
        this.formRef.current.setFieldsValue({
          hypertension: 0,
        });
        await this.setState((prevState) => ({
            hedisisSelected1: !prevState.hedisisSelected1,
            heartdisease: 0,
        }));
        this.formRef.current.setFieldsValue({
            heartdisease: 0,
        });
        await this.setState({ smokingHistory: 4 });
        this.formRef.current.setFieldsValue({
            smokingHistory: 4,
        });
        await this.setState({ bmi: 25.19 });
        this.formRef.current.setFieldsValue({
            bmi: 25.19,
        });
        await this.setState({ hbA1cLevel: 6.6 });
        this.formRef.current.setFieldsValue({
            hbA1cLevel: 6.6,
        });
        await this.setState({ bloodGlucoseLevel: 140 });
        this.formRef.current.setFieldsValue({
            bloodGlucoseLevel: 140,
        });
        console.log("Data set to example 1");
        // console.log(this.state.gender);
    }

    onClickExample2 = async () => {
        console.log("clicked example 2");
        await this.setState((prevState) => ({
            femaleisSelected2: !prevState.femaleisSelected2,
            gender: 1,
        }));
            this.formRef.current.setFieldsValue({
            gender: 1,
        });
        if (this.state.maleisSelected1) {
            await this.setState((prevState) => ({
                maleisSelected1: !prevState.maleisSelected1,
                gender: 1,
            }));
        }
        await this.setState((prevState) => ({
            currentPrediction: "Your prediction will be displayed here",
        }));
        
        if (this.state.hyperisSelected1) {
            await this.setState((prevState) => ({
                hyperisSelected1: !prevState.hyperisSelected1,
            }));
        }
        await this.setState({ age: 90 });
        this.formRef.current.setFieldsValue({
            age: 90,
        });
        await this.setState((prevState) => ({
            hyperisSelected2: !prevState.hyperisSelected2,
            hypertension: 1,
        }));
        this.formRef.current.setFieldsValue({
            hypertension: 1,
        });
        
        if (this.state.hedisisSelected1) {
            await this.setState((prevState) => ({
                hedisisSelected1: !prevState.hedisisSelected1,
            }));
        }
        await this.setState((prevState) => ({
            hedisisSelected2: !prevState.hedisisSelected2,
            heartdisease: 1,
        }));
        this.formRef.current.setFieldsValue({
            heartdisease: 1,
        });
        await this.setState({ smokingHistory: 12 });
        this.formRef.current.setFieldsValue({
            smokingHistory: 12,
        });
        await this.setState({ bmi: 40 });
        this.formRef.current.setFieldsValue({
            bmi: 40,
        });
        await this.setState({ hbA1cLevel: 10 });
        this.formRef.current.setFieldsValue({
            hbA1cLevel: 10,
        });
        await this.setState({ bloodGlucoseLevel: 260 });
        this.formRef.current.setFieldsValue({
            bloodGlucoseLevel: 260,
        });
        console.log("Data set to example 2");
        // console.log(this.state.gender);
    }

    onClickhypertension1 = () => {
        this.setState((prevState) => ({
            hyperisSelected1: !prevState.hyperisSelected1,
            hypertension: 0,
        }));
        this.formRef.current.setFieldsValue({
          hypertension: 0,
        });
      };
    
    onClickhypertension2 = () => {
        this.setState((prevState) => ({
            hyperisSelected2: !prevState.hyperisSelected2,
            hypertension: 1,
        }));
        this.formRef.current.setFieldsValue({
            hypertension: 1,
        });
    };
    onClickheartdis2 = () => {
        this.setState((prevState) => ({
            hedisisSelected2: !prevState.hedisisSelected2,
            heartdisease: 1,
        }));
        this.formRef.current.setFieldsValue({
            heartdisease: 1,
        });
    };

    onClickheartdis1 = () => {
        this.setState((prevState) => ({
            hedisisSelected1: !prevState.hedisisSelected1,
            heartdisease: 0,
        }));
        this.formRef.current.setFieldsValue({
            heartdisease: 0,
        });
    };
    
    onClickFemale = () => {
        this.setState((prevState) => ({
          femaleisSelected2: !prevState.femaleisSelected2,
          gender: 1,
        }));
        this.formRef.current.setFieldsValue({
          gender: 1,
        });
      };
    
    onClickMale = () => {
        this.setState((prevState) => ({
            maleisSelected1: !prevState.maleisSelected1,
            gender: 0,
        }));
        this.formRef.current.setFieldsValue({
            gender: 0,
        });
      };

    onClickQuetions = async () => {
        console.log("clicked ask quetions");

        // const response = await this.onAskQuestions();
        // // console.log(response);
        // this.setState({ currentAnswer: response });
        // console.log(this.state.currentAnswer);
        // // console.log(this.state.currentAnswer.created)

        await this.onAskQuestions();
        console.log(this.state.currentAnswer);
    }

    onSetAnswers = async (response) => {
        await this.setState({ currentAnswer : response });
        console.log(this.state.currentAnswer);
    }

    onClickModels = async () => {
        console.log("clicked quote models");

        const response = await this.onQuoteModels();
        console.log(response);
    }

    onChangeQuestions = async (e) => {
        await this.setState({ currentQuestion : e.target.value });
        console.log(this.state.currentQuestion);
    }

    onChangeModels = async e => {
        await this.setState({ currentQuote : e.target.value });
        console.log(this.state.currentQuote);
    }

    onChangeGender = async (e) => {
        await this.setState({ gender : e });
        console.log(this.state.gender);
    }

    onChangeAge = async e => {
        await this.setState({ age : e});
        console.log(this.state.age);
    }

    onChangeHypertension = async e => {
        await this.setState({ hypertension : e });
        console.log(this.state.hypertension);
    }

    onChangeHeartdisease = async e => {
        await this.setState({ heartdisease : e });
        console.log(this.state.heartdisease);
    }

    onChangeSmokingHistory = async e => {
        await this.setState({ smokingHistory : e });
        console.log(this.state.smokingHistory);
    }

    onChangeBmi = async e => {
        await this.setState({ bmi : e });
        console.log(this.state.bmi);
    }

    onChangeHbA1cLevel = async e => {
        await this.setState({ hbA1cLevel : e });
        console.log(this.state.hbA1cLevel);
    }

    onChangeBloodGlucoseLevel = async e => {
        await this.setState({ BloodGlucoseLevel : e });
        console.log(this.state.BloodGlucoseLevel);
    }

    // onAskQuestions = async () => {
    //     return fetch(`${ASK_QUETIONS_URL}${this.state.currentQuestion}`, {
    //         method: 'GET',
    //         headers: {
    //         'Content-Type': 'application/json',
    //         },
    //     }).then((response) => {
    //         if (response.status !== 200) {
    //             throw Error('Fail to request the answer from the server');
    //         }

    //         return response.json(); // Return the promise directly
    //     }).then((result) => {
    //         console.log(result);
    //         this.setState({ currentAnswer: result }); // Set the result when the promise resolves
    //         // console.log(this.state.currentAnswer);
    //         return result; // Return the result value
    //     });
    // }

    onAskQuestions = () => {
        axios.get(`${ASK_QUETIONS_URL}${this.state.currentQuestion}`, {
            headers: {
            'Content-Type': 'application/json',
            },
        }).then((response) => {
            if (response.status !== 200) {
                throw Error('Fail to request the answer from the server');
            }

            
            console.log(response);
            this.setState({ currentAnswer: response.data.text}); // Set the result when the promise resolves
            // console.log(this.state.currentAnswer);
            return response; // Return the result value
        });
    }

    onClickPrediction = () => {
        this.setState({ isLoading: true });
        var data = [[this.state.gender, this.state.age, this.state.hypertension, this.state.heartdisease, this.state.smokingHistory, this.state.bmi, this.state.hbA1cLevel, this.state.bloodGlucoseLevel]]
        var matrix = { 'data': data }
        console.log(matrix);
        console.log(JSON.stringify(matrix));
        axios.post(`${QUOTE_MODEL_URL}`, {
            headers: {
            'Content-Type': 'application/json',
            },
            body: JSON.stringify(matrix)
        }).then((response) => {
            this.setState({ isLoading: false });
            if (response.status !== 200) {
                throw Error('Fail to request the answer from the server');
            }

            
            // console.log(response);
            this.setState({ currentPrediction: response.data.prediction}); // Set the result when the promise resolves
            console.log(this.state.currentPrediction+text1);
            return response; // Return the result value
        });
    }

    onQuoteModels = async (data) => {
        return fetch(`${QUOTE_MODEL_URL}`, {
            method: 'post',
            headers: {
            'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        }).then((response) => {
            if (response.status !== 200) {
                throw Error('Fail to request the prediction from the server');
            }

            return response.json();
        })
    }

    render() {
        const { isLoading } = this.state;
        return (
            <div className="Main" style={{fontWeight: "bold"}}>
                <Tabs defaultActiveKey = "prediction">
                    <Tabs.TabPane tab="Prediction" key="prediction">
                        <p className="larger-text">IntelliHealth Prediction</p>
                        <p style={{fontWeight: "normal", fontSize: "15px"}}>
                            Please input the following information to get a prediction of your risk of getting diabetes.
                        </p>
                        
                        <Form ref={this.formRef}>
                           
                            <Row gutter={[16, 0]}>
                            <Col span={12}>
                                <Form.Item
                                label="Gender"
                                name="gender"
                                rules={[
                                    {
                                    required: true,
                                    message: 'Please select an option',
                                    validator: (_, value) =>
                                        value ? Promise.resolve() : Promise.reject('Please select an option'),
                                    },
                                ]}
                                labelAlign="left"
                                wrapperCol={{ span: 24 }} // Adjust the span value to control the width of the buttons container
                                >
                                <SelectionButton
                                    isSelected={this.state.maleisSelected1}
                                    onSelect={this.onClickMale}
                                    label="Male"
                                />
                                <SelectionButton
                                    isSelected={this.state.femaleisSelected2}
                                    onSelect={this.onClickFemale}
                                    label="Female"
                                />
                                </Form.Item>
                            </Col>
                            <Col span={12}>
                                <Form.Item
                                label="Heart Disease"
                                name="heartdisease"
                                rules={[
                                    {
                                    required: true,
                                    message: 'Please select an option',
                                    validator: (_, value) =>
                                        value ? Promise.resolve() : Promise.reject('Please select an option'),
                                    },
                                ]}
                                labelAlign="left"
                                wrapperCol={{ span: 16 }} // Adjust the span value to control the width of the buttons container
                                >
                                <SelectionButton
                                    isSelected={this.state.hedisisSelected2}
                                    onSelect={this.onClickheartdis2}
                                    label="Yes"
                                />
                                <SelectionButton
                                    isSelected={this.state.hedisisSelected1}
                                    onSelect={this.onClickheartdis1}
                                    label="No"
                                />
                                </Form.Item>
                            </Col>
                            </Row>
                            <Row gutter={[16, 0]}>
                            <Col span={12}>
                                <Form.Item
                                label="Hypertension"
                                name="hypertension"
                                rules={[
                                    {
                                    required: true,
                                    message: 'Please select an option',
                                    validator: (_, value) =>
                                        value ? Promise.resolve() : Promise.reject('Please select an option'),
                                    },
                                ]}
                                labelAlign="left"
                                wrapperCol={{ span: 17 }} // Adjust the span value to control the width of the buttons container
                                >
                                <SelectionButton
                                    isSelected={this.state.hyperisSelected2}
                                    onSelect={this.onClickhypertension2}
                                    label="Yes"
                                />
                                <SelectionButton
                                    isSelected={this.state.hyperisSelected1}
                                    onSelect={this.onClickhypertension1}
                                    label="No"
                                />
                                </Form.Item>
                            </Col>
                            <Col span={12}>
                                <Form.Item label="Age (years)" name="age" initialValue={80} rules={[
                                                                                {
                                                                                required: true,
                                                                                message: 'Please select an option',
                                                                                validator: (_, value) =>
                                                                                    value ? Promise.resolve() : Promise.reject('Please select an option'),
                                                                                },
                                                                            ]}  
                                                                            labelAlign="left"
                                wrapperCol={{ span: 24 }} >
                                    <InputNumber min={0} max={100} onChange={this.onChangeAge} precision={0}/>
                                </Form.Item>
                            </Col>
                            </Row>
                            <Row gutter={[16, 0]}>
                            <Col span={12}>
                            <Form.Item label="Smoking History (years)" name="smokingHistory" initialValue={4} rules={[
                                                                            {
                                                                            required: true,
                                                                            message: 'Please select an option',
                                                                            validator: (_, value) =>
                                                                                value ? Promise.resolve() : Promise.reject('Please select an option'),
                                                                            },
                                                                        ]}  
                                                                        labelAlign="left" wrapperCol={{ span: 8 }} >
                                   <InputNumber min={0} max={100} onChange={this.onChangeSmokingHistory} precision={2}/>
                            </Form.Item>
                            </Col>
                            <Col span={12}>
                                <Form.Item label="BMI (kg/m2)" name="bmi" initialValue={25.19} rules={[
                                                                                {
                                                                                required: true,
                                                                                message: 'Please select an option',
                                                                                validator: (_, value) =>
                                                                                    value ? Promise.resolve() : Promise.reject('Please select an option'),
                                                                                },
                                                                            ]}  
                                                                            labelAlign="left" wrapperCol={{ span: 29 }} >
                                    <InputNumber min={0} max={100} onChange={this.onChangeBmi} precision={2}/>
                                </Form.Item>
                            </Col>
                            </Row>
                            <Row gutter={[16, 0]}>
                            <Col span={12}>
                            <Form.Item label="HbA1c Level" name="hbA1cLevel" initialValue={6.6} rules={[{ required: true, message: 'Please input valid numbers'}]} labelAlign="left" wrapperCol={{ span: 19 }}>
                                <InputNumber min={0} max={100} onChange={this.onChangeHbA1cLevel} precision={2}/>
                            </Form.Item>
                            </Col>
                            <Col span={12}>
                                <Form.Item label="Blood Glucose Level (mg/dL)" name="bloodGlucoseLevel" initialValue={140} rules={[{ required: true, message: 'Please input valid numbers'}]} labelAlign="left" wrapperCol={{ span: 1 }}>
                                    <InputNumber min={0} max={600} onChange={this.onChangeBloodGlucoseLevel} precision={2}/>
                                </Form.Item>
                            </Col>
                            </Row>
                    
                        </Form>

                        <Button  type="primary" htmlType="submit" onClick={this.onClickExample1} style={{ margin: 20 }}> Example 1 </Button>

                        <Button  type="primary" htmlType="submit" onClick={this.onClickExample2} style={{  margin: 20 }}> Example 2 </Button>

                        <p></p>

                        <Button  type="primary" htmlType="submit" onClick={this.onClickPrediction}> Get Prediction </Button>
                        

                       
                        
       

                <div>
                    <Card title="Prediction: " bordered={false} style={{ width: 800, margin: 10}}>
                        {isLoading ? <LoadingSpinner /> : 
                            <p style={{ textAlign: 'left' }}>
                                {this.state.currentPrediction !== null ? (
                                    this.state.currentPrediction.split('\n').map((paragraph, index) => (
                                    <React.Fragment key={index}>
                                        {index > 0 ? (
                                        <span style={{ marginLeft: '20px' }}>{paragraph}</span>
                                        ) : (
                                        <span style={{ display: 'block', textAlign: 'center' }}>{paragraph}</span>
                                        )}
                                        <br />
                                    </React.Fragment>
                                    ))
                                ) : (
                                    <span>No prediction available.</span>
                                )}
                            </p>
                        }
                    </Card>

            </div>
            <p>
            </p>
                </Tabs.TabPane>
                <p>
                    
                </p>
                    <Tabs.TabPane tab="Chatbot" key="chatbot">
                        <p className="larger-text">IntelliHealth Prediction</p>
                        <p style={{fontWeight: "normal", fontSize: "15px"}}>
                            If you have any question, feel free to ask any questions about the diabetes
                        </p>


                        <TextArea showCount maxLength={100} onChange={this.onChangeQuestions} style={{ width: 800, height: 50}} />
                        <p>

                        </p>

                        <Button type="primary" htmlType="submit" onClick={this.onClickQuetions}> Send it </Button>

                        <p>

                        </p>

                        <div>
                            <Card title="ChatBot Response: " bordered={false} style={{ width: 800, margin: 20 }}>
                                <p >
                                    {this.state.currentAnswer}
                                </p>
                            </Card>

                        </div>
                    </Tabs.TabPane>
                </Tabs>
            </div>
        );
    }
}
export default Physician;