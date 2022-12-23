import { Component } from '@angular/core';
import { ApiService } from './api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'Логгер';
  description = 'Логгер';

  devices = [];

  constructor(private apiService: ApiService) {
    this.apiService.getDeviceList().subscribe((res: any) => {
      this.devices = res;
    });
  }
}
