import { Injectable } from '@angular/core';
import { webSocket, WebSocketSubject } from 'rxjs/webSocket';
import { environment } from '../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class WebSocketService {
  private socket1: WebSocketSubject<any>;
  
  constructor() {
        // Access environment variables
        const apiBaseUrl = environment.apiBaseUrl;
        const wsBaseUrl = environment.wsBaseUrl;
        const deviceId = environment.deviceId;
    
    // Replace the URL with your WebSocket server URL
      this.socket1 = webSocket(wsBaseUrl+'/ws/device/'+deviceId+'/') 
  }
  getMessageDevice(){
    
    return this.socket1.asObservable();
  }
  sendMessage(message: any): void {
    this.socket1.next(message);
  }
}
