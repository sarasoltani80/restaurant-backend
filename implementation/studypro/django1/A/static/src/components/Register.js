import React, { Fragment } from "react";
import Input from "./Input";
import {
    VALIDATOR_REQUIRE,
    VALIDATOR_MINLENGTH,
    VALIDATOR_MAXLENGTH,
    VALIDATOR_EMAIL
  } from './Validators';

const Register = () => {
    return (
        <Fragment>
            <form>
                <Input
                    type="text"
                    label="Username"
                    id="username"
                    validators={[VALIDATOR_MINLENGTH(4), VALIDATOR_MAXLENGTH(12)]}
                    errorText="Username must be at least 4 and At most 12 characters!(and not empty)"
                />

                <Input
                    type="text"
                    label="Email"
                    id="email"
                    validators={[VALIDATOR_EMAIL()]}
                    errorText="Email must be valid!(example@example.example)"
                />
                
                <Input
                    type="text"
                    label="Password"
                    id="password"
                    validators={[VALIDATOR_MINLENGTH(8)]}
                    errorText="Password must be at least 8 chatacters!(and not empty)"
                />

                <Input
                    type="text"
                    label="First name"
                    id="firstname"
                    validators={[VALIDATOR_REQUIRE()]}
                    errorText="First name must be valid!(and not empty)"
                />

                <Input
                    type="text"
                    label="Last name"
                    id="lastname"
                    validators={[VALIDATOR_REQUIRE()]}
                    errorText="Last name must be valid!(and not empty)"
                />
                <button type="submit">Register</button>
            </form>
        </Fragment>
    );
}; 

export default Register;