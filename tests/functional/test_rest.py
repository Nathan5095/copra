    # def test_get_server_time(self):
    #     async def go():
    #         async with Client(self.loop) as client:
    #             time = await client.get_server_time()
    #             self.assertIsInstance(time, dict)
    #             self.assertIn('iso', time)
    #             self.assertIn('epoch', time)
    #             self.assertIsInstance(time['iso'], str)
    #             self.assertIsInstance(time['epoch'], float)
                
    #     self.loop.run_until_complete(go())
    
    # @unittest.skipUnless(TEST_AUTH, "Authentication credentials not provided.")
    # def test_list_accounts(self):
    #     async def go():
    #         async with Client(self.loop) as client:
    #             with self.assertRaises(ValueError):
    #                 accounts = await client.list_accounts()
            
    #         async with Client(self.loop, auth=True, key=KEY, secret=SECRET, 
    #                           passphrase=PASSPHRASE) as client:
    #             accounts = await client.list_accounts()
    #             self.assertIsInstance(accounts, list)
    #             self.assertIsInstance(accounts[0], dict)
    #             self.assertIn('id', accounts[0])
    #             self.assertIn('currency', accounts[0])
    #             self.assertIn('balance', accounts[0])
    #             self.assertIn('available', accounts[0])
    #             self.assertIn('hold', accounts[0])
    #             self.assertIn('profile_id', accounts[0])
    
    #     self.loop.run_until_complete(go())
    
    # @unittest.skipUnless(TEST_AUTH and TEST_ACCOUNT, "Auth credentials and test account ID required")
    # def test_get_account(self):
    #     async def go():
    #         async with Client(self.loop) as client:
    #             with self.assertRaises(ValueError):
    #                 acount = await client.get_account(TEST_ACCOUNT)
            
    #         async with Client(self.loop, auth=True, key=KEY, secret=SECRET, 
    #                           passphrase=PASSPHRASE) as client:
    #             account = await client.get_account(TEST_ACCOUNT)
    #             self.assertIsInstance(account, dict)
    #             self.assertIn('id', account)
    #             self.assertIn('currency', account)
    #             self.assertIn('balance', account)
    #             self.assertIn('available', account)
    #             self.assertIn('hold', account)
    #             self.assertIn('profile_id', account)
                
    #     self.loop.run_until_complete(go())
    
    # @unittest.skipUnless(TEST_AUTH and TEST_ACCOUNT, "Auth credentials and test account ID required")
    # def test_get_account_activity(self):
    #     async def go():
    #         async with Client(self.loop) as client:
    #             with self.assertRaises(ValueError):
    #                 activity = await client.get_account_history(TEST_ACCOUNT)
                    
    #         async with Client(self.loop, auth=True, key=KEY, secret=SECRET, 
    #                           passphrase=PASSPHRASE) as client:
    #             results = await client.get_account_history(TEST_ACCOUNT)
    #             self.assertEqual(len(results), 3)
    #             self.assertIsInstance(results[0], list)
    #             self.assertIsInstance(results[0][0], dict)
    #             self.assertIsInstance(results[1], str)
    #             self.assertIsInstance(results[2], str)
                
    #             next_results = await client.get_account_history(TEST_ACCOUNT, after=results[2])
    #             self.assertEqual(len(next_results), 3)
    #             self.assertIsInstance(next_results[0], list)
    #             self.assertIsInstance(next_results[0][0], dict)
    #             self.assertIsInstance(next_results[1], str)
    #             self.assertIsInstance(next_results[2], str)
    #             self.assertLess(next_results[0][0]['id'], results[0][-1]['id'])
                
    #             prev_results = await client.get_account_history(TEST_ACCOUNT, before=next_results[1])
    #             self.assertEqual(prev_results, results)
                
    #             ten_results = await client.get_account_history(TEST_ACCOUNT, limit=10)
    #             self.assertEqual(len(ten_results[0]), 10)
                
    #     self.loop.run_until_complete(go())
    
    #@patch('aiohttp.ClientSession.get')
    # def test_get_holds(self, mock_get):
    #     async def go():
    #         async with Client(self.loop) as client:
    #             with self.assertRaises(ValueError):
    #                 holds, before, after = await client.get_holds('ACCOUNT ID')
                    
    #         holds = [{'key', 'hold place holder'}] 
            
    #         mo = MagicMock()
    #         mo.__aenter__ = MagicMock(return_value = mo)
    #         mo.__aexit__ = MagicMock(return_value = None)
    #         mock_get.return_value = mo
            

    #         async with Client(self.loop, auth=True, key=MOCK_KEY, 
    #                           secret=MOCK_SECRET, 
    #                           passphrase=MOCK_PASSPHRASE) as client:
    #                 holds, before, after = await client.get_holds('ACCOUNT ID')
                    
    #                 print(holds)
        
    #     self.loop.run_until_complete(go())