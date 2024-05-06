#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;
bool solution(vector<string> phone_book) {
	sort(phone_book.begin(), phone_book.end());
	for (int i = 0; i < phone_book.size()-1; i++)
			if (0 == phone_book[i+1].find(phone_book[i])) return false;
	return true;
}