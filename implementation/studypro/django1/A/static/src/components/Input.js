import React from 'react';
import {useState} from 'react';
import {validate} from './Validators';
import './sign.css';

const Input = props => {
  const [inputStates, setInputStates] = useState({
    untouched: true,
    validity: true
  });

  const [styleClass, setStyleClass] = useState('form-input');

  const inputBlurHandler = (event) => {
    const value = event.target.value;
    setInputStates(prevState => {
      return {
        ...prevState,
        untouched: false,
        validity: validate(value, props.validators)
      }
    });
    if (!validate(value, props.validators)) {
      setStyleClass('form-input form-input--invalid');
    } else {
      setStyleClass('form-input');
    }
  };

  const inputChangeHandler = (event) => {
    const value = event.target.value;
    setInputStates(prevState => {
      return {
        ...prevState,
        validity: validate(value, props.validators)
      }
    });
    if (!validate(value, props.validators)) {
      setStyleClass('form-input form-input--invalid');
    } else {
      setStyleClass('form-input');
    }
  }

   return (
     <div className={styleClass} data-testid="form-input">
       <label htmlFor={props.label}>{props.label}</label>
       <input type={props.type} id={props.label} onBlur={inputBlurHandler} onChange={inputChangeHandler} />
       {inputStates.validity === false && <p>{props.errorText}</p>}
     </div>
   )
};

export default Input;
