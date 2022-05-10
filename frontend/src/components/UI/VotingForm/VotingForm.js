import React, { useState } from 'react';
import APIClient from "../../../services/APIClient";

const VotingForm = () => {
    const [ title, setTitle ] = useState("");
    const [ description, setDescription ] = useState("");
    const [ deadline, setDeadline ] = useState("");

    const client = new APIClient();

    const titleChangeHandler = (event) => {
        setTitle(event.target.value);
    }

    const descriptionChangeHandler = (event) => {
        setDescription(event.target.value);
    }

    const deadlineChangeHandler = (event) => {
        setDeadline(event.target.value);
    }

    const addVotingHandler = (event) => {
        event.preventDefault();

        client.addVoting(title, description, deadline).then(() => {
            console.log('voting added');
        });
    }

    return (
        <div>
            <form>
                <label>
                    Title:
                    <input type="text" name="name" onChange={ titleChangeHandler } />
                </label>
                <label>
                    Desription:
                    <input type="text" name="name" onChange={ descriptionChangeHandler } />
                </label>
                <label>
                    Deadline:
                    <input type="date" name="name"  onChange={ deadlineChangeHandler } />
                </label>
                <input type="submit" value="Submit" onClick={ addVotingHandler }/>
            </form>
        </div>
    );
};

export default VotingForm;
