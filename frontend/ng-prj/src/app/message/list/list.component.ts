import { Component, OnInit } from '@angular/core';

import { ApiService } from './../../api.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.scss']
})
export class ListComponent implements OnInit {

  constructor(private apiService: ApiService, private route: ActivatedRoute) { 
    this.route.params.subscribe((params) => {
      if (params.hasOwnProperty('deviceId')) {
        this.getMessageList({ device: params['deviceId'] });
      } else {
        this.getMessageList({});
      }
    });
  }

  ngOnInit(): void {}

  messageList = { results: [] };

  getMessageList(params: any) {
    this.apiService.getMessageList(params).subscribe((res: any) => {
      this.messageList = res;
    });
  }

}
