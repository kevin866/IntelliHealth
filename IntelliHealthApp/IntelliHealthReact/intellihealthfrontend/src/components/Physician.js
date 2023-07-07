import React, {Component} from 'react';
import { Button, Input, Card} from 'antd';
import axios from 'axios';

const ASK_QUETIONS_URL = 'http://127.0.0.1:5000/api/v1/chat/'
const QUOTE_MODEL_URL = 'http://127.0.0.1:5000/api/v1/model/prediction'
const { TextArea } = Input;

class Physician extends Component {
    constructor(props) {
        super(props);
        // define state for the components states
        this.state = {
            currentQuestion: null,
            currentQuote: null,
            currentAnswer: "Your answer will be displayed here",
        }
    }

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
        return (
            <div className="Main" style={{fontWeight: "bold"}}>
                IntelliHealthBot
                <p style={{fontWeight: "normal", fontSize: "15px"}}>
                    Feel free to ask any questions about the diabetes
                </p>

                <TextArea showCount maxLength={100} onChange={this.onChangeQuestions} style={{ width: 800, height: 300 }} />
                <p>

                </p>

                <Button type="primary" htmlType="submit" onClick={this.onClickQuetions}> Send it </Button>

                <p>

                </p>

                <div>
                    <Card title="ChatBot Response: " bordered={false} style={{ width: 800 }}>
                        <p >
                            {this.state.currentAnswer}
                        </p>
                    </Card>

                </div>



            </div>
        );
    }
}
export default Physician;