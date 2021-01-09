import React from 'react';
import './square.css'



class Square extends React.Component {

    constructor(props) {
        super(props)
    }

    render() {
      return <div style={{minWidth: this.props.width, minHeight: this.props.height}}className="square_container">
          <div className="square_image">
              <img width={this.props.width} height={this.props.height} src={this.props.image}></img>
              <div>{this.props.text}</div>
          </div>
      </div>;
    }
  }

export default Square;