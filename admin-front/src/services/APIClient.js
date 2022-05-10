"use strict";

import AxiosWrapper from "./AxiosWrapper";
import Storage from "./Storage";

class APIClient {
    constructor() {
        this.storage = new Storage(window.localStorage)
    }

    fetchVotings() {
        const wrapper = new AxiosWrapper('http://localhost:8000/adminApp/votings/');
        return Promise.resolve(
            wrapper.get()
                .catch((error) => {
                    this.storage.clear();
                    console.error(error);
                    return Promise.reject(error);
                })
        )
    }

    addVoting(title, description, deadline) {
        const wrapper = new AxiosWrapper('http://localhost:8000/adminApp/votings/');
        if (title.length > 0 && description.length > 0) {
            return Promise.resolve(
                wrapper.post(
                    {
                        title: title,
                        description: description,
                        deadline: deadline
                    }
                ).catch((error) => console.error(error.response) )
            )
        } else {
            return Promise.reject("Please, enter information");
        }
    }

    deleteVoting(id) {
        const wrapper = new AxiosWrapper('http://localhost:8000/adminApp/votings/' + id);
        return Promise.resolve(
            wrapper.delete().catch((error) => {
                console.error(error);
                return Promise.reject(error);
            })
        )
    }

    fetchVoters() {
        const wrapper = new AxiosWrapper('http://localhost:8000/adminApp/voters/');
        return Promise.resolve(
            wrapper.get()
                .catch((error) => {
                    this.storage.clear();
                    console.error(error);
                    return Promise.reject(error);
                })
        )
    }

    addVoter(pubkey, voting) {
        const wrapper = new AxiosWrapper('http://localhost:8000/adminApp/voters/');
        if (pubkey.length > 0) {
            return Promise.resolve(
                wrapper.post(
                    {
                        pubkey: pubkey,
                        voting: voting
                    }
                ).catch((error) => console.error(error.response) )
            )
        } else {
            return Promise.reject("Please, enter information");
        }
    }

    deleteVoter(id) {
        const wrapper = new AxiosWrapper('http://localhost:8000/adminApp/voters/' + id);
        return Promise.resolve(
            wrapper.delete().catch((error) => {
                console.error(error);
                return Promise.reject(error);
            })
        )
    }

    fetchVotingOption() {
        const wrapper = new AxiosWrapper('http://localhost:8000/adminApp/voting_options/');
        return Promise.resolve(
            wrapper.get()
                .catch((error) => {
                    this.storage.clear();
                    console.error(error);
                    return Promise.reject(error);
                })
        )
    }

    addVotingOption(title, description, voting, pubkey, privkey) {
        const wrapper = new AxiosWrapper('http://localhost:8000/adminApp/voting_options/');
        if (pubkey.length > 0) {
            return Promise.resolve(
                wrapper.post(
                    {
                        title: title,
                        description: description,
                        voting: voting,
                        pubkey: pubkey,
                        privkey: privkey
                    }
                ).catch((error) => console.error(error.response) )
            )
        } else {
            return Promise.reject("Please, enter information");
        }
    }

    deleteVotingOption(id) {
        const wrapper = new AxiosWrapper('http://localhost:8000/adminApp/voting_options/' + id);
        return Promise.resolve(
            wrapper.delete().catch((error) => {
                console.error(error);
                return Promise.reject(error);
            })
        )
    }
}

export default APIClient;