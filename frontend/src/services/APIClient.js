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
}

export default APIClient;