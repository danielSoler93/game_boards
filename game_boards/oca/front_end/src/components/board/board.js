import React from 'react';
import Square from '../square/square'
import pozo from '../images/pozo.jpeg';
import "./board.css"




class Board extends React.Component {

    constructor(props) {
        super(props)
    }

    render() {
      return <div className="board_container">
            <Square text="Inicio" width={100} height={100} image={pozo}></Square>
            <Square text="Pozo" width={100} height={100} image={pozo}></Square>
          </div>;
    }
  }

export default Board;