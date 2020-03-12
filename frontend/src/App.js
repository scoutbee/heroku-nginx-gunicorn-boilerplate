import React, { useState, useEffect } from 'react';

import Container from 'react-bootstrap/Container'
import Jumbotron from 'react-bootstrap/Jumbotron'
import Button from 'react-bootstrap/Button'

const VALUE_FETCHING = "loading..."

const App = () => {
  const [currentValue, setCurrentValue] = useState(VALUE_FETCHING)
  const catchFetchErrors = (err) => err.then(err => {
    console.log(err)
    alert(err)
  })
  useEffect(() => {
    setCurrentValue(VALUE_FETCHING)
    fetch("/api/v1/counter/get")
      .then(resp => resp.ok ? resp.json() : Promise.reject(resp.text()))
      .then(resp => {
        setCurrentValue(resp.value)
      })
      .catch(catchFetchErrors)
  }, [])
  const handleIncreaseCounter = () => {
    setCurrentValue(VALUE_FETCHING)
    fetch("/api/v1/counter/increase", {
      method: "POST"
    })
      .then(resp => resp.ok ? resp.json() : Promise.reject(resp.text()))
      .then(resp => {
        setCurrentValue(resp.value)
      })
      .catch(catchFetchErrors)
  }
  return (
    <Container className="pt-3">
      <Jumbotron>
        <h1>Würzburg Web Week bees counter</h1>
        <p>
          This is a minimal application which demonstrates how React will interact
          with Django in a simple way by increasing a counter stored in a database.
        </p>
        <p>Number of bees in the hive: {currentValue}</p>
        <p>
          <Button variant="primary" onClick={handleIncreaseCounter}>Increase value</Button>
        </p>
      </Jumbotron>
    </Container>
  );
}

export default App;
