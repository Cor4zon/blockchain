import React, { useState } from 'react';
import APIClient from "../../../services/APIClient";

const VotingOption = ({ voting }) => {
    const [ pubkey, setPubkey ] = useState("");
    const [ privkey, setPrivkey ] = useState("");
    const [ title, setTitle ] = useState("");
    const [ description, setDescription ] = useState("");

    const client = new APIClient();

    const titleChangeHandler = (event) => {
        setTitle(event.target.value);
    }

    const descriptionChangeHandler = (event) => {
        setDescription(event.target.value);
    }

    const pubkeyChangeHandler = (event) => {
        setPubkey(event.target.value);
    }

    const privkeyChangeHandler = (event) => {
        setPrivkey(event.target.value);
    }

    const addVotingOptionHandler = (event) => {
        event.preventDefault();

        client.addVotingOption(title, description, voting, pubkey, privkey).then(() => {
            console.log('voting option added');
        });
    }

    return (
        <>
            <form>
                <label>
                    Title:
                    <input type="text" name="name" onChange={ titleChangeHandler } />
                </label>
                <label>
                    Description:
                    <input type="text" name="name" onChange={ descriptionChangeHandler } />
                </label>
                <label>
                    Public key:
                    <input type="text" name="name" onChange={ pubkeyChangeHandler } />
                </label>
                <label>
                    Private key:
                    <input type="text" name="name" onChange={ privkeyChangeHandler } />
                </label>

                <input type="submit" value="Submit" onClick={ addVotingOptionHandler }/>
            </form>
        </>
    );
};

export default VotingOption;
