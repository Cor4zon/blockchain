import React, { useState } from 'react';
import APIClient from "../../../services/APIClient";

const VoterForm = ({ voting }) => {
    const [ pubkey, setPubkey ] = useState("");
    const client = new APIClient();

    const pubkeyChangeHandler = (event) => {
        setPubkey(event.target.value);
    }

    const addVoterHandler = (event) => {
        event.preventDefault();
        client.addVoter(pubkey, voting).then(() => {
            console.log('voter added');
        });
    }

    return (
        <>
            <form>
                <label>
                    public key:
                    <input type="text" name="name" onChange={ pubkeyChangeHandler } />
                </label>
                <input type="submit" value="Submit" onClick={ addVoterHandler }/>
            </form>
        </>
    );
};

export default VoterForm;
