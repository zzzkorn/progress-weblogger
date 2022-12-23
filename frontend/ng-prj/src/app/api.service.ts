import { Injectable } from '@angular/core';
import { environment } from './../environments/environment';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})

export class ApiService {

  constructor(private http: HttpClient) { }

  getDeviceList() {
    return this.http.get(`${environment.backendUrl}v1/logger/devices/`);
  }

  getMessageList(params: any) {
    if (params.hasOwnProperty('device')) {
      return this.http.get(
        `${environment.backendUrl}v1/logger/messages/?device=${params.device}`
      );
    }
    return this.http.get(`${environment.backendUrl}v1/logger/messages/`);
  }
}
